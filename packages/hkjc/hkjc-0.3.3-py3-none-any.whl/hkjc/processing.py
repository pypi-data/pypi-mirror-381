"""Functions to batch process trades into dataframes for analysis.
"""
from __future__ import annotations
from typing import Tuple, List

from .live_odds import live_odds
from .qpbanker import win_probability, expected_value, average_odds
from .optimization import _pareto_filter
from .harville_model import HarvilleOptimizer

import polars as pl
import numpy as np
from itertools import combinations
from tqdm import tqdm


def _all_subsets(lst): return [list(x) for r in range(
    1, len(lst)+1) for x in combinations(lst, r)]  # list subsets of a list


def _process_single_qp_trade(banker: int, covered: List[int], odds_pla: List[float], odds_qpl: List[float], rebate: float) -> Tuple[int, List, float, float]:
    """Process a single qp trade.
    """
    win_prob = win_probability(odds_pla, banker, covered)
    exp_value = expected_value(odds_pla, odds_qpl, banker, covered, rebate)
    ave_odds = average_odds(odds_qpl, banker, covered)
    return (banker, covered, win_prob, exp_value, ave_odds)


def generate_all_qp_trades(date: str, venue_code: str, race_number: int, rebate: float = 0.12, harville_fit=True) -> pl.DataFrame:
    """Generate all possible qp tickets for the specified race.

    Args:
        date (str): Date in 'YYYY-MM-DD' format.
        venue_code (str): Venue code, e.g., 'ST' for Shatin, 'HV' for Happy Valley.
        race_number (int): Race number.
        rebate (float, optional): The rebate percentage. Defaults to 0.12.
        harville_fit (bool, optional): Whether to fit the odds using Harville model. Defaults to True.

    Returns:
        pl.DataFrame: DataFrame with all possible trades and their metrics.
    """

    odds = live_odds(date, venue_code, race_number,
                     odds_type=['PLA', 'QPL', 'WIN', 'QIN'])
    N = len(odds['PLA'])
    candidates = np.arange(1, N+1)

    if harville_fit:
        ho = HarvilleOptimizer(N)
        prob = {k: np.nan_to_num(1/v, 0) for k,v in odds.items()}
        fit_res = ho.fit(prob['WIN'], prob['QIN'],
                         prob['QPL'], prob['PLA'])
        if fit_res['success']:
            odds['PLA'] = np.nan_to_num(1/fit_res['b_fitted'], posinf=0)
            odds['QPL'] = np.nan_to_num(1/fit_res['Q_fitted'], posinf=0)

    results = [_process_single_qp_trade(banker, covered, odds['PLA'], odds['QPL'], rebate)
               for banker in tqdm(candidates, desc="Processing bankers")
               for covered in _all_subsets(candidates[candidates != banker])]

    df = (pl.DataFrame(results, schema=['Banker', 'Covered', 'WinProb', 'ExpValue', 'AvgOdds'])
          .with_columns(pl.col('Covered').list.len().alias('NumCovered')))

    return df


def generate_pareto_qp_trades(date: str, venue_code: str, race_number: int, rebate: float = 0.12, groupby: List[str] = []) -> pl.DataFrame:
    """Generate qp tickets that are Pareto optimal for the specified race.

    Args:
        date (str): Date in 'YYYY-MM-DD' format.
        venue_code (str): Venue code, e.g., 'ST' for Shatin, 'HV' for Happy Valley.
        race_number (int): Race number.
        rebate (float, optional): The rebate percentage. Defaults to 0.12.
        groupby (List[str], optional): Columns to group by when determining Pareto optimality. Defaults to [] (global optimal).

    Returns:
        pl.DataFrame: DataFrame with all Pareto trades and their metrics.
    """
    df = generate_all_qp_trades(date, venue_code, race_number, rebate)
    pareto_df = _pareto_filter(df, groupby=groupby, by=[
                               'WinProb', 'ExpValue'], maximize=True)
    return pareto_df
