"""Functions to fetch and process data from HKJC
"""
from __future__ import annotations
from typing import Tuple, List

from .harville_model import fit_harville_to_odds

import requests
from cachetools.func import ttl_cache
import numpy as np
from datetime import datetime as dt

ENDPOINT = "https://info.cld.hkjc.com/graphql/base/"

LIVEODDS_PAYLOAD = {
    "operationName": "racing",
    "variables": {"date": None, "venueCode": None, "raceNo": None, "oddsTypes": None},
    "query": """
query racing($date: String, $venueCode: String, $oddsTypes: [OddsType], $raceNo: Int) {
    raceMeetings(date: $date, venueCode: $venueCode) {
        pmPools(oddsTypes: $oddsTypes, raceNo: $raceNo) {
            id
            status
            sellStatus
            oddsType
            lastUpdateTime
            guarantee
            minTicketCost
            name_en
            name_ch
            leg {
                number
                races
            }
            cWinSelections {
                composite
                name_ch
                name_en
                starters
            }
            oddsNodes {
                combString
                oddsValue
                hotFavourite
                oddsDropValue
                bankerOdds {
                    combString
                    oddsValue
                }
            }
        }
    }
}""",
}


@ttl_cache(maxsize=12, ttl=30)
def _fetch_live_odds(date: str, venue_code: str, race_number: int, odds_type: Tuple[str] = ('PLA', 'QPL')) -> Tuple[dict]:
    """Fetch live odds data from HKJC GraphQL endpoint."""
    payload = LIVEODDS_PAYLOAD.copy()
    payload["variables"] = payload["variables"].copy()
    payload["variables"]["date"] = date
    payload["variables"]["venueCode"] = venue_code
    payload["variables"]["raceNo"] = race_number
    payload["variables"]["oddsTypes"] = odds_type

    headers = {
        "Origin": "https://bet.hkjc.com",
        "Referer": "https://bet.hkjc.com",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "python-hkjc-fetch/0.1",
    }

    r = requests.post(ENDPOINT, json=payload, headers=headers, timeout=10)
    if r.status_code != 200:
        raise RuntimeError(f"Request failed: {r.status_code} - {r.text}")

    meetings = r.json().get("data", {}).get("raceMeetings", [])

    return [
        {"HorseID": node["combString"], "Type": pool.get(
            "oddsType"), "Odds": float(node["oddsValue"])}
        for meeting in meetings
        for pool in meeting.get("pmPools", [])
        for node in pool.get("oddsNodes", [])
    ]


def live_odds(date: str, venue_code: str, race_number: int, odds_type: List[str] = ['PLA', 'QPL'], fit_harville=False) -> dict:
    """Fetch live odds as numpy arrays.

    Args:
        date (str): Date in 'YYYY-MM-DD' format.
        venue_code (str): Venue code, e.g., 'ST' for Shatin, 'HV' for Happy Valley.
        race_number (int): Race number.
        odds_type (List[str]): Types of odds to fetch. Default is ['PLA', 'QPL']. Currently the following types are supported:
            - 'WIN': Win odds
            - 'PLA': Place odds
            - 'QIN': Quinella odds
            - 'QPL': Quinella Place odds
        fit_harville (bool): Whether to fit the odds using Harville model. Default is False.

    Returns:
        dict: Dictionary with keys as odds types and values as numpy arrays containing the odds.
            If odds_type is 'WIN','PLA', returns a 1D array of place odds.
            If odds_type is 'QIN','QPL', returns a 2D array of quinella place odds. 
    """
    # validate date format
    try:
        dt.strptime(date, "%Y-%m-%d")
    except Exception:
        raise ValueError("Date must be in 'YYYY-MM-DD' format")

    mandatory_types = ['WIN','PLA','QIN','QPL'] if fit_harville else ['PLA']

    data = _fetch_live_odds(date, venue_code, race_number,
                            odds_type=tuple(set(mandatory_types+odds_type)))

    # use place odds to determine number of horses
    pla_data = [entry for entry in data if entry["Type"] == "PLA"]
    N = len(pla_data)

    odds = {'WIN': np.full(N, np.nan, dtype=float),
            'PLA': np.full(N, np.nan, dtype=float),
            'QIN': np.full((N, N), np.nan, dtype=float),
            'QPL': np.full((N, N), np.nan, dtype=float)}

    for entry in data:
        if entry["Type"] in ["QIN", "QPL"]:
            horse_ids = list(map(int, entry["HorseID"].split(",")))
            odds[entry["Type"]][horse_ids[0] - 1, horse_ids[1] - 1] = entry["Odds"]
            odds[entry["Type"]][horse_ids[1] - 1, horse_ids[0] - 1] = entry["Odds"]
        elif entry["Type"] in ["PLA","WIN"]:
            odds[entry["Type"]][int(entry["HorseID"]) - 1] = entry["Odds"]

    if fit_harville:
        fit_res = fit_harville_to_odds(
            W_obs=odds['WIN'],
            Qin_obs=odds['QIN'],
            Q_obs=odds['QPL'],
            b_obs=odds['PLA']
        )
        if fit_res['success']:
            odds['PLA'] = np.nan_to_num(1/fit_res['b_fitted'], posinf=0)
            odds['QPL'] = np.nan_to_num(1/fit_res['Q_fitted'], posinf=0)
            odds['WIN'] = np.nan_to_num(1/fit_res['W_fitted'], posinf=0)
            odds['QIN'] = np.nan_to_num(1/fit_res['Qin_fitted'], posinf=0)
        else:
            print(f"[WARNING] Harville model fitting failed: {fit_res.get('message','')}")

    return {t: odds[t] for t in odds_type}
