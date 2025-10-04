"""
PatX - Pattern eXtraction for Time Series Feature Engineering

A Python package for extracting polynomial patterns from time series data
to create meaningful features for machine learning models.
"""

from .core import feature_extraction
from .models import LightGBMModel
from .data import load_remc_data

__version__ = "0.2.5"
__author__ = "Jonas Wolber"
__email__ = "jonascw@web.de"

__all__ = [
    "feature_extraction",
    "LightGBMModel",
    "load_remc_data"
]