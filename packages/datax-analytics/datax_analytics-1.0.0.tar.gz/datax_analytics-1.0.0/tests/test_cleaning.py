"""
Tests for the DataX cleaning module.
"""

import pytest
import pandas as pd
import numpy as np
from datax.cleaning import DataCleaner
import tempfile
import os


class TestDataCleaner:
    """Test cases for DataCleaner class."""
    
    def test_init_with_data(self, sample_dataframe):
        """Test DataCleaner initialization with data."""
        cleaner = DataCleaner(sample_dataframe)
        assert cleaner.data is not None
        assert cleaner.original_data is not None
        assert len(cleaner.cleaning_log) == 0
    
    def test_init_without_data(self):
        """Test DataCleaner initialization without data."""
        cleaner = DataCleaner()
        assert cleaner.data is None
        assert cleaner.original_data is None
    
    def test_load_data(self, sample_dataframe):
        """Test loading data into cleaner."""
        cleaner = DataCleaner()
        result = cleaner.load_data(sample_dataframe)
        
        assert result is cleaner  # Method chaining
        assert cleaner.data is not None
        assert cleaner.original_data is not None
        assert len(cleaner.cleaning_log) == 1
        assert "Data loaded" in cleaner.cleaning_log[0]
    
    def test_get_info(self, sample_dataframe):
        """Test getting data information."""
        cleaner = DataCleaner(sample_dataframe)
        info = cleaner.get_info()
        
        assert 'shape' in info
        assert 'columns' in info
        assert 'dtypes' in info
        assert 'memory_usage' in info
        assert 'missing_values' in info
        assert 'duplicates' in info
        assert info['shape'] == sample_dataframe.shape
    
    def test_get_missing_summary(self, sample_dataframe):
        """Test getting missing value summary."""
        cleaner = DataCleaner(sample_dataframe)
        missing_info = cleaner.get_missing_summary()
        
        assert 'total_missing' in missing_info
        assert 'missing_by_column' in missing_info
        assert 'missing_percentage_by_column' in missing_info
        assert 'columns_with_missing' in missing_info
    
    def test_get_duplicate_count(self, sample_dataframe):
        """Test getting duplicate count."""
        cleaner = DataCleaner(sample_dataframe)
        duplicate_count = cleaner.get_duplicate_count()
        
        assert isinstance(duplicate_count, int)
        assert duplicate_count >= 0
    
    def test_handle_missing_values_auto(self, sample_dataframe):
        """Test automatic missing value handling."""
        cleaner = DataCleaner(sample_dataframe)
        original_missing = cleaner.data.isnull().sum().sum()
        
        cleaner.handle_missing_values(method='auto')
        
        new_missing = cleaner.data.isnull().sum().sum()
        assert new_missing <= original_missing
        assert len(cleaner.cleaning_log) > 0
    
    def test_handle_missing_values_drop(self, sample_dataframe):
        """Test dropping rows with missing values."""
        cleaner = DataCleaner(sample_dataframe)
        original_shape = cleaner.data.shape
        
        cleaner.handle_missing_values(method='drop')
        
        new_shape = cleaner.data.shape
        assert new_shape[0] <= original_shape[0]
        assert cleaner.data.isnull().sum().sum() == 0
    
    def test_handle_missing_values_fill(self, sample_dataframe):
        """Test filling missing values."""
        cleaner = DataCleaner(sample_dataframe)
        
        cleaner.handle_missing_values(method='fill', fill_value=0)
        
        assert cleaner.data.isnull().sum().sum() == 0
    
    def test_handle_missing_values_interpolate(self, sample_dataframe):
        """Test interpolating missing values."""
        cleaner = DataCleaner(sample_dataframe)
        
        cleaner.handle_missing_values(method='interpolate')
        
        # Interpolation should reduce missing values
        assert cleaner.data.isnull().sum().sum() < sample_dataframe.isnull().sum().sum()
    
    def test_handle_missing_values_specific_columns(self, sample_dataframe):
        """Test handling missing values in specific columns."""
        cleaner = DataCleaner(sample_dataframe)
        columns = ['numeric_col', 'missing_col']
        
        cleaner.handle_missing_values(method='fill', fill_value=0, columns=columns)
        
        # Check that specified columns have no missing values
        for col in columns:
            assert cleaner.data[col].isnull().sum() == 0
    
    def test_remove_duplicates(self, sample_dataframe):
        """Test removing duplicate rows."""
        cleaner = DataCleaner(sample_dataframe)
        original_count = len(cleaner.data)
        
        cleaner.remove_duplicates()
        
        new_count = len(cleaner.data)
        assert new_count <= original_count
        assert cleaner.data.duplicated().sum() == 0
    
    def test_remove_duplicates_subset(self, sample_dataframe):
        """Test removing duplicates based on specific columns."""
        cleaner = DataCleaner(sample_dataframe)
        
        cleaner.remove_duplicates(subset=['categorical_col'])
        
        # Should have fewer or equal rows
        assert len(cleaner.data) <= len(sample_dataframe)
    
    def test_detect_outliers_iqr(self, sample_dataframe):
        """Test outlier detection using IQR method."""
        cleaner = DataCleaner(sample_dataframe)
        outliers = cleaner.detect_outliers(method='iqr')
        
        assert isinstance(outliers, dict)
        for col, outlier_indices in outliers.items():
            assert isinstance(outlier_indices, list)
            assert all(isinstance(idx, int) for idx in outlier_indices)
    
    def test_detect_outliers_zscore(self, sample_dataframe):
        """Test outlier detection using Z-score method."""
        cleaner = DataCleaner(sample_dataframe)
        outliers = cleaner.detect_outliers(method='zscore', threshold=2.0)
        
        assert isinstance(outliers, dict)
    
    def test_detect_outliers_modified_zscore(self, sample_dataframe):
        """Test outlier detection using modified Z-score method."""
        cleaner = DataCleaner(sample_dataframe)
        outliers = cleaner.detect_outliers(method='modified_zscore')
        
        assert isinstance(outliers, dict)
    
    def test_handle_outliers_remove(self, sample_dataframe):
        """Test removing outliers."""
        cleaner = DataCleaner(sample_dataframe)
        original_count = len(cleaner.data)
        
        cleaner.handle_outliers(method='iqr', action='remove')
        
        new_count = len(cleaner.data)
        assert new_count <= original_count
    
    def test_handle_outliers_cap(self, sample_dataframe):
        """Test capping outliers."""
        cleaner = DataCleaner(sample_dataframe)
        original_count = len(cleaner.data)
        
        cleaner.handle_outliers(method='iqr', action='cap')
        
        # Should have same number of rows
        assert len(cleaner.data) == original_count
    
    def test_handle_outliers_replace(self, sample_dataframe):
        """Test replacing outliers."""
        cleaner = DataCleaner(sample_dataframe)
        original_count = len(cleaner.data)
        
        cleaner.handle_outliers(method='iqr', action='replace', replacement_value=0)
        
        # Should have same number of rows
        assert len(cleaner.data) == original_count
    
    def test_convert_data_types_auto(self, sample_dataframe):
        """Test automatic data type conversion."""
        cleaner = DataCleaner(sample_dataframe)
        
        cleaner.convert_data_types(auto_convert=True)
        
        # Should have converted some types
        assert len(cleaner.cleaning_log) > 0
    
    def test_convert_data_types_manual(self, sample_dataframe):
        """Test manual data type conversion."""
        cleaner = DataCleaner(sample_dataframe)
        type_mapping = {'categorical_col': 'category'}
        
        cleaner.convert_data_types(type_mapping=type_mapping)
        
        assert cleaner.data['categorical_col'].dtype == 'category'
    
    def test_validate_data_basic(self, sample_dataframe):
        """Test basic data validation."""
        cleaner = DataCleaner(sample_dataframe)
        validation_results = cleaner.validate_data()
        
        assert 'passed' in validation_results
        assert 'errors' in validation_results
        assert 'warnings' in validation_results
        assert 'summary' in validation_results
        assert isinstance(validation_results['passed'], bool)
    
    def test_validate_data_with_rules(self, sample_dataframe, validation_rules):
        """Test data validation with custom rules."""
        cleaner = DataCleaner(sample_dataframe)
        
        # Modify data to test validation
        cleaner.data.loc[0, 'age'] = 200  # Invalid age
        
        validation_results = cleaner.validate_data(rules=validation_rules)
        
        assert 'passed' in validation_results
        # Should fail due to invalid age
        assert not validation_results['passed']
        assert len(validation_results['errors']) > 0
    
    def test_validate_data_strict(self, sample_dataframe, validation_rules):
        """Test strict data validation."""
        cleaner = DataCleaner(sample_dataframe)
        
        # Modify data to test validation
        cleaner.data.loc[0, 'age'] = 200  # Invalid age
        
        with pytest.raises(ValueError):
            cleaner.validate_data(rules=validation_rules, strict=True)
    
    def test_get_cleaning_summary(self, sample_dataframe):
        """Test getting cleaning summary."""
        cleaner = DataCleaner(sample_dataframe)
        
        # Perform some cleaning operations
        cleaner.handle_missing_values(method='auto')
        cleaner.remove_duplicates()
        
        summary = cleaner.get_cleaning_summary()
        
        assert 'original_shape' in summary
        assert 'current_shape' in summary
        assert 'cleaning_operations' in summary
        assert 'data_info' in summary
        assert len(summary['cleaning_operations']) > 0
    
    def test_reset(self, sample_dataframe):
        """Test resetting to original data."""
        cleaner = DataCleaner(sample_dataframe)
        original_shape = cleaner.data.shape
        
        # Perform some operations
        cleaner.handle_missing_values(method='drop')
        cleaner.remove_duplicates()
        
        # Reset
        cleaner.reset()
        
        assert cleaner.data.shape == original_shape
        assert len(cleaner.cleaning_log) == 0
    
    def test_save_cleaned_data_csv(self, sample_dataframe, temp_file):
        """Test saving cleaned data as CSV."""
        cleaner = DataCleaner(sample_dataframe)
        output_path = temp_file.replace('.csv', '_output.csv')
        
        cleaner.save_cleaned_data(output_path, format='csv')
        
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
    
    def test_save_cleaned_data_excel(self, sample_dataframe, temp_file):
        """Test saving cleaned data as Excel."""
        cleaner = DataCleaner(sample_dataframe)
        output_path = temp_file.replace('.csv', '_output.xlsx')
        
        cleaner.save_cleaned_data(output_path, format='excel')
        
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
    
    def test_save_cleaned_data_json(self, sample_dataframe, temp_file):
        """Test saving cleaned data as JSON."""
        cleaner = DataCleaner(sample_dataframe)
        output_path = temp_file.replace('.csv', '_output.json')
        
        cleaner.save_cleaned_data(output_path, format='json')
        
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
    
    def test_save_cleaned_data_parquet(self, sample_dataframe, temp_file):
        """Test saving cleaned data as Parquet."""
        cleaner = DataCleaner(sample_dataframe)
        output_path = temp_file.replace('.csv', '_output.parquet')
        
        cleaner.save_cleaned_data(output_path, format='parquet')
        
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
    
    def test_save_cleaned_data_invalid_format(self, sample_dataframe, temp_file):
        """Test saving with invalid format."""
        cleaner = DataCleaner(sample_dataframe)
        output_path = temp_file.replace('.csv', '_output.txt')
        
        with pytest.raises(ValueError):
            cleaner.save_cleaned_data(output_path, format='txt')
    
    def test_error_handling_no_data(self):
        """Test error handling when no data is loaded."""
        cleaner = DataCleaner()
        
        with pytest.raises(ValueError):
            cleaner.handle_missing_values()
        
        with pytest.raises(ValueError):
            cleaner.remove_duplicates()
        
        with pytest.raises(ValueError):
            cleaner.detect_outliers()
    
    def test_error_handling_invalid_methods(self, sample_dataframe):
        """Test error handling with invalid methods."""
        cleaner = DataCleaner(sample_dataframe)
        
        with pytest.raises(ValueError):
            cleaner.handle_missing_values(method='invalid')
        
        with pytest.raises(ValueError):
            cleaner.handle_outliers(method='invalid')
    
    def test_error_handling_missing_fill_value(self, sample_dataframe):
        """Test error handling when fill_value is missing."""
        cleaner = DataCleaner(sample_dataframe)
        
        with pytest.raises(ValueError):
            cleaner.handle_missing_values(method='fill')
    
    def test_error_handling_missing_replacement_value(self, sample_dataframe):
        """Test error handling when replacement_value is missing."""
        cleaner = DataCleaner(sample_dataframe)
        
        with pytest.raises(ValueError):
            cleaner.handle_outliers(action='replace')
    
    def test_comprehensive_cleaning_pipeline(self, messy_dataframe):
        """Test a comprehensive cleaning pipeline."""
        cleaner = DataCleaner(messy_dataframe)
        original_shape = cleaner.data.shape
        
        # Comprehensive cleaning
        cleaner.handle_missing_values(method='auto') \
               .remove_duplicates() \
               .handle_outliers(method='iqr', action='cap') \
               .convert_data_types(auto_convert=True) \
               .validate_data()
        
        # Check results
        assert cleaner.data.shape[0] <= original_shape[0]
        assert len(cleaner.cleaning_log) > 0
        
        # Check that data is cleaner
        assert cleaner.data.isnull().sum().sum() < messy_dataframe.isnull().sum().sum()
        assert cleaner.data.duplicated().sum() == 0
    
    def test_series_handling(self, sample_series):
        """Test handling of pandas Series."""
        cleaner = DataCleaner(sample_series)
        
        # Should work with Series
        info = cleaner.get_info()
        assert 'shape' in info
        
        # Should handle missing values
        cleaner.handle_missing_values(method='auto')
        assert cleaner.data is not None
    
    def test_empty_dataframe(self, mock_data):
        """Test handling of empty DataFrame."""
        cleaner = DataCleaner(mock_data['empty_df'])
        
        # Should handle empty DataFrame gracefully
        info = cleaner.get_info()
        assert info['shape'] == (0, 0)
        
        # Should not crash on operations
        cleaner.handle_missing_values(method='auto')
        cleaner.remove_duplicates()
    
    def test_single_column_dataframe(self, mock_data):
        """Test handling of single column DataFrame."""
        cleaner = DataCleaner(mock_data['single_col_df'])
        
        # Should work with single column
        info = cleaner.get_info()
        assert info['shape'][1] == 1
        
        # Should handle operations
        cleaner.handle_missing_values(method='auto')
        cleaner.convert_data_types(auto_convert=True)
    
    def test_all_nan_dataframe(self, mock_data):
        """Test handling of DataFrame with all NaN values."""
        cleaner = DataCleaner(mock_data['all_nan_df'])
        
        # Should handle all NaN DataFrame
        info = cleaner.get_info()
        assert info['shape'] == (2, 2)
        
        # Should handle operations gracefully
        cleaner.handle_missing_values(method='auto')
        assert cleaner.data is not None
