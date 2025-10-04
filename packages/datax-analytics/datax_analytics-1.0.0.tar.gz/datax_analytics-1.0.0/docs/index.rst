DataX Documentation
===================

Welcome to DataX, the advanced data analytics package for Python!

DataX provides comprehensive tools for data cleaning, statistical analysis, and visualization with both programmatic and command-line interfaces.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   user_guide/index
   api_reference/index
   examples/index
   contributing
   changelog

Features
--------

* **Advanced Data Cleaning**: Missing value handling, outlier detection, data validation, type conversion
* **Comprehensive Statistics**: Descriptive statistics, correlation analysis, hypothesis testing, regression analysis
* **Rich Visualizations**: Statistical plots, interactive charts, customizable themes, export capabilities
* **Command Line Interface**: Full CLI support with interactive mode and batch processing
* **High Performance**: Optimized for large datasets with efficient memory usage

Quick Start
-----------

Install DataX:

.. code-block:: bash

   pip install datax

Basic usage:

.. code-block:: python

   import pandas as pd
   from datax import DataCleaner, DataAnalyzer, DataVisualizer

   # Load your data
   df = pd.read_csv('your_data.csv')

   # Data Cleaning
   cleaner = DataCleaner(df)
   cleaner.handle_missing_values(method='auto')
   cleaner.remove_duplicates()
   cleaned_data = cleaner.data

   # Statistical Analysis
   analyzer = DataAnalyzer(cleaned_data)
   desc_stats = analyzer.get_descriptive_stats()
   correlation = analyzer.get_correlation_matrix()

   # Visualization
   visualizer = DataVisualizer(cleaned_data)
   visualizer.plot_distribution('column_name')
   visualizer.plot_correlation_heatmap()

Command Line Interface:

.. code-block:: bash

   # Load data and get information
   datax load data.csv info

   # Clean data with auto missing value handling
   datax load data.csv clean --missing auto

   # Perform statistical analysis
   datax load data.csv stats --descriptive --correlation

   # Create visualizations
   datax load data.csv viz --distributions --correlation-heatmap

   # Interactive mode
   datax interactive

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
