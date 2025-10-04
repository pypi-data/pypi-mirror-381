Data Cleaning Guide
===================

DataX provides comprehensive data cleaning capabilities through the ``DataCleaner`` class. This guide covers all cleaning operations and best practices.

Getting Started
---------------

Initialize a DataCleaner with your data:

.. code-block:: python

   import pandas as pd
   from datax import DataCleaner
   
   # Load your data
   df = pd.read_csv('your_data.csv')
   
   # Initialize cleaner
   cleaner = DataCleaner(df)
   
   # Or initialize without data and load later
   cleaner = DataCleaner()
   cleaner.load_data(df)

Data Information
----------------

Get comprehensive information about your data:

.. code-block:: python

   # Get basic info
   info = cleaner.get_info()
   print(f"Shape: {info['shape']}")
   print(f"Columns: {info['columns']}")
   print(f"Memory usage: {info['memory_usage']:,} bytes")
   
   # Get missing value summary
   missing_info = cleaner.get_missing_summary()
   print(f"Total missing values: {missing_info['total_missing']}")
   print("Columns with missing values:")
   for col, count in missing_info['columns_with_missing'].items():
       print(f"  {col}: {count}")
   
   # Get duplicate count
   duplicate_count = cleaner.get_duplicate_count()
   print(f"Duplicate rows: {duplicate_count}")

Missing Value Handling
----------------------

DataX provides several methods for handling missing values:

Automatic Handling
~~~~~~~~~~~~~~~~~~

The automatic method intelligently chooses the best approach:

.. code-block:: python

   cleaner.handle_missing_values(method='auto')
   
   # This will:
   # - Drop rows if >50% missing
   # - Fill categorical columns with mode
   # - Fill numeric columns with median

Drop Missing Values
~~~~~~~~~~~~~~~~~~~

Remove rows with missing values:

.. code-block:: python

   # Drop rows with any missing values
   cleaner.handle_missing_values(method='drop')
   
   # Drop rows with missing values in specific columns
   cleaner.handle_missing_values(method='drop', columns=['age', 'salary'])

Fill Missing Values
~~~~~~~~~~~~~~~~~~~

Fill missing values with a specific value:

.. code-block:: python

   # Fill with a specific value
   cleaner.handle_missing_values(method='fill', fill_value=0)
   
   # Fill different columns with different values
   cleaner.handle_missing_values(method='fill', 
                                fill_value={'age': 25, 'salary': 50000})

Interpolation
~~~~~~~~~~~~~

Use interpolation for time series or ordered data:

.. code-block:: python

   cleaner.handle_missing_values(method='interpolate')

Duplicate Removal
-----------------

Remove duplicate rows:

.. code-block:: python

   # Remove all duplicates, keeping first occurrence
   cleaner.remove_duplicates()
   
   # Remove duplicates based on specific columns
   cleaner.remove_duplicates(subset=['id', 'name'])
   
   # Keep last occurrence instead of first
   cleaner.remove_duplicates(keep='last')
   
   # Remove all duplicates (keep none)
   cleaner.remove_duplicates(keep=False)

Outlier Detection and Handling
------------------------------

Detect outliers using various methods:

.. code-block:: python

   # Detect outliers using IQR method
   outliers = cleaner.detect_outliers(method='iqr', threshold=1.5)
   print("Outliers found:")
   for col, indices in outliers.items():
       print(f"{col}: {len(indices)} outliers")
   
   # Detect outliers using Z-score
   outliers = cleaner.detect_outliers(method='zscore', threshold=2.0)
   
   # Detect outliers using modified Z-score
   outliers = cleaner.detect_outliers(method='modified_zscore', threshold=3.5)

Handle outliers in different ways:

.. code-block:: python

   # Remove outliers
   cleaner.handle_outliers(method='iqr', action='remove')
   
   # Cap outliers at IQR boundaries
   cleaner.handle_outliers(method='iqr', action='cap')
   
   # Replace outliers with a specific value
   cleaner.handle_outliers(method='iqr', action='replace', 
                          replacement_value=0)

Data Type Conversion
--------------------

Convert data types automatically or manually:

.. code-block:: python

   # Auto-convert obvious types
   cleaner.convert_data_types(auto_convert=True)
   
   # Manual type conversion
   type_mapping = {
       'category_col': 'category',
       'date_col': 'datetime',
       'numeric_col': 'float64'
   }
   cleaner.convert_data_types(type_mapping=type_mapping)

Data Validation
---------------

Validate data against custom rules:

.. code-block:: python

   # Define validation rules
   validation_rules = {
       "age_range": {
           "type": "range",
           "column": "age",
           "min": 18,
           "max": 120
       },
       "salary_positive": {
           "type": "range",
           "column": "salary",
           "min": 0
       },
       "unique_id": {
           "type": "unique",
           "column": "id"
       },
       "email_format": {
           "type": "regex",
           "column": "email",
           "pattern": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
       }
   }
   
   # Validate data
   validation_results = cleaner.validate_data(rules=validation_rules)
   
   if validation_results['passed']:
       print("Data validation passed!")
   else:
       print("Validation errors:")
       for error in validation_results['errors']:
           print(f"  - {error}")
   
   # Strict validation (raises exception on failure)
   try:
       cleaner.validate_data(rules=validation_rules, strict=True)
   except ValueError as e:
       print(f"Validation failed: {e}")

Comprehensive Cleaning Pipeline
-------------------------------

Combine multiple cleaning operations:

.. code-block:: python

   # Complete cleaning pipeline
   cleaner = DataCleaner(df)
   
   # Step 1: Handle missing values
   cleaner.handle_missing_values(method='auto')
   
   # Step 2: Remove duplicates
   cleaner.remove_duplicates()
   
   # Step 3: Handle outliers
   cleaner.handle_outliers(method='iqr', action='cap')
   
   # Step 4: Convert data types
   cleaner.convert_data_types(auto_convert=True)
   
   # Step 5: Validate data
   validation_rules = {
       "age_range": {"type": "range", "column": "age", "min": 18, "max": 120},
       "salary_positive": {"type": "range", "column": "salary", "min": 0}
   }
   cleaner.validate_data(rules=validation_rules)
   
   # Get cleaned data
   cleaned_data = cleaner.data

Method Chaining
---------------

DataX supports method chaining for cleaner code:

.. code-block:: python

   cleaned_data = (DataCleaner(df)
                   .handle_missing_values(method='auto')
                   .remove_duplicates()
                   .handle_outliers(method='iqr', action='cap')
                   .convert_data_types(auto_convert=True)
                   .data)

Cleaning Summary
----------------

Get a summary of all cleaning operations:

.. code-block:: python

   summary = cleaner.get_cleaning_summary()
   print(f"Original shape: {summary['original_shape']}")
   print(f"Final shape: {summary['current_shape']}")
   print("Operations performed:")
   for operation in summary['cleaning_operations']:
       print(f"  - {operation}")

Reset to Original Data
----------------------

Reset to the original data if needed:

.. code-block:: python

   # Reset to original state
   cleaner.reset()
   
   # Now cleaner.data is back to the original data
   assert cleaner.data.equals(df)

Saving Cleaned Data
-------------------

Save cleaned data in various formats:

.. code-block:: python

   # Save as CSV
   cleaner.save_cleaned_data('cleaned_data.csv', format='csv')
   
   # Save as Excel
   cleaner.save_cleaned_data('cleaned_data.xlsx', format='excel')
   
   # Save as JSON
   cleaner.save_cleaned_data('cleaned_data.json', format='json')
   
   # Save as Parquet
   cleaner.save_cleaned_data('cleaned_data.parquet', format='parquet')

Best Practices
--------------

1. **Always inspect your data first** using ``get_info()`` and ``get_missing_summary()``
2. **Use automatic missing value handling** for most cases
3. **Be careful with outlier removal** - consider capping instead
4. **Validate your data** after cleaning to ensure quality
5. **Save intermediate results** for reproducibility
6. **Document your cleaning steps** for future reference

Common Pitfalls
---------------

1. **Over-cleaning**: Don't remove too much data
2. **Ignoring context**: Consider the business context when handling outliers
3. **Data leakage**: Be careful when filling missing values in time series
4. **Type conversion errors**: Check data types after conversion
5. **Memory issues**: Use chunking for very large datasets

Performance Tips
----------------

1. **Use appropriate methods** for your data size
2. **Avoid unnecessary operations** on large datasets
3. **Use vectorized operations** when possible
4. **Consider memory usage** for very large datasets
5. **Profile your cleaning pipeline** for optimization
