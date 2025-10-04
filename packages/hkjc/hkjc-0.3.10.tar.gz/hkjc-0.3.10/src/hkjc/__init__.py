"""Top-level package for hkjc tools.

This module re-exports commonly used symbols from the submodules.
"""
from importlib.metadata import version as _version

__all__ = ["live_odds", "qpbanker",
           "generate_all_qp_trades", "generate_all_pla_trades", "pareto_filter",
                        "speedpro_energy", "speedmap", "harveille_model"]

try:
    __version__ = _version(__name__)
except Exception:  # pragma: no cover - best-effort version resolution
    __version__ = "0.0.0"

from .live_odds import live_odds
from .processing import generate_all_qp_trades, generate_all_pla_trades
from .optimization import pareto_filter
from .speedpro import speedmap, speedpro_energy
from . import harville_model
