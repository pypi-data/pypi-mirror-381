"""
PatX - Pattern eXtraction for Time Series Feature Engineering

A Python package for extracting polynomial patterns from time series data
to create meaningful features for machine learning models.
"""

from .core import PatternExtractor
from .models import LightGBMModel, get_model, evaluate_model_performance
from .data import load_remc_data
from . import visualizations

__version__ = "0.2.3"
__author__ = "Jonas Wolber"
__email__ = "jonascw@web.de"

__all__ = [
    "PatternExtractor",
    "LightGBMModel",
    "get_model",
    "evaluate_model_performance",
    "load_remc_data",
    "visualizations"
]
