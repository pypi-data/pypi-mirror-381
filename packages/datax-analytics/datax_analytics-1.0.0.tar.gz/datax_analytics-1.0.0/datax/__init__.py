"""
DataX - Advanced Data Analytics Package

A comprehensive Python package for data cleaning, statistical analysis, 
and visualization with CLI interface and advanced features.

Author: DataX Team
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "DataX Team"
__email__ = "contact@datax.dev"
__license__ = "MIT"

# Import main modules for easy access
from .cleaning import DataCleaner
from .stats import DataAnalyzer
from .viz import DataVisualizer
from .cli import main

# Define what gets imported with "from datax import *"
__all__ = [
    "DataCleaner",
    "DataAnalyzer", 
    "DataVisualizer",
    "main",
    "__version__",
    "__author__",
    "__email__",
    "__license__"
]

# Package metadata
__title__ = "datax-analytics"
__description__ = "Advanced Data Analytics Package with cleaning, statistics, and visualization"
__url__ = "https://github.com/datax/datax"
__download_url__ = f"https://github.com/datax/datax/archive/v{__version__}.tar.gz"
__keywords__ = ["data", "analytics", "cleaning", "statistics", "visualization", "cli"]
__classifiers__ = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
