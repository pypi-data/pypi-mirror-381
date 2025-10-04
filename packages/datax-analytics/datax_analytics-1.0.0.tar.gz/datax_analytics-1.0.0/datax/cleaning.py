"""
Data Cleaning Module for DataX Package

This module provides comprehensive data cleaning functionality including:
- Missing value handling
- Outlier detection and treatment
- Data type conversion
- Duplicate removal
- Data validation
- Advanced cleaning pipelines
"""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Any, Optional, Tuple
import warnings
from scipy import stats
from sklearn.preprocessing import StandardScaler, RobustScaler
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataCleaner:
    """
    Advanced data cleaning class with comprehensive cleaning methods.
    
    This class provides a wide range of data cleaning operations including
    missing value handling, outlier detection, data validation, and more.
    """
    
    def __init__(self, data: Union[pd.DataFrame, pd.Series] = None):
        """
        Initialize DataCleaner with optional data.
        
        Args:
            data: pandas DataFrame or Series to clean
        """
        self.data = data.copy() if data is not None else None
        self.original_data = data.copy() if data is not None else None
        self.cleaning_log = []
        
    def load_data(self, data: Union[pd.DataFrame, pd.Series]) -> 'DataCleaner':
        """
        Load data into the cleaner.
        
        Args:
            data: pandas DataFrame or Series
            
        Returns:
            self for method chaining
        """
        self.data = data.copy()
        self.original_data = data.copy()
        self.cleaning_log.append(f"Data loaded: {data.shape}")
        logger.info(f"Data loaded: {data.shape}")
        return self
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get comprehensive information about the data.
        
        Returns:
            Dictionary with data information
        """
        if self.data is None:
            return {"error": "No data loaded"}
            
        info = {
            "shape": self.data.shape,
            "columns": list(self.data.columns) if hasattr(self.data, 'columns') else None,
            "dtypes": self.data.dtypes.to_dict() if hasattr(self.data, 'dtypes') else str(self.data.dtype),
            "memory_usage": self.data.memory_usage(deep=True).sum(),
            "missing_values": self.get_missing_summary(),
            "duplicates": self.get_duplicate_count(),
            "numeric_columns": self._get_numeric_columns(),
            "categorical_columns": self._get_categorical_columns(),
            "datetime_columns": self._get_datetime_columns()
        }
        return info
    
    def get_missing_summary(self) -> Dict[str, Any]:
        """
        Get summary of missing values.
        
        Returns:
            Dictionary with missing value information
        """
        if self.data is None:
            return {}
            
        if isinstance(self.data, pd.Series):
            missing_count = self.data.isnull().sum()
            missing_pct = (missing_count / len(self.data)) * 100
            return {
                "total_missing": missing_count,
                "missing_percentage": missing_pct
            }
        
        missing_data = self.data.isnull().sum()
        missing_pct = (missing_data / len(self.data)) * 100
        
        return {
            "total_missing": missing_data.sum(),
            "missing_by_column": missing_data.to_dict(),
            "missing_percentage_by_column": missing_pct.to_dict(),
            "columns_with_missing": missing_data[missing_data > 0].to_dict()
        }
    
    def get_duplicate_count(self) -> int:
        """
        Get count of duplicate rows.
        
        Returns:
            Number of duplicate rows
        """
        if self.data is None:
            return 0
        return self.data.duplicated().sum()
    
    def _get_numeric_columns(self) -> List[str]:
        """Get list of numeric columns."""
        if self.data is None or isinstance(self.data, pd.Series):
            return []
        return self.data.select_dtypes(include=[np.number]).columns.tolist()
    
    def _get_categorical_columns(self) -> List[str]:
        """Get list of categorical columns."""
        if self.data is None or isinstance(self.data, pd.Series):
            return []
        return self.data.select_dtypes(include=['object', 'category']).columns.tolist()
    
    def _get_datetime_columns(self) -> List[str]:
        """Get list of datetime columns."""
        if self.data is None or isinstance(self.data, pd.Series):
            return []
        return self.data.select_dtypes(include=['datetime64']).columns.tolist()
    
    def handle_missing_values(self, 
                            method: str = 'auto',
                            fill_value: Any = None,
                            columns: Optional[List[str]] = None) -> 'DataCleaner':
        """
        Handle missing values using various methods.
        
        Args:
            method: Method to handle missing values ('auto', 'drop', 'fill', 'interpolate')
            fill_value: Value to fill missing values with
            columns: Specific columns to process (None for all columns)
            
        Returns:
            self for method chaining
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if columns is None:
            columns = self.data.columns.tolist() if hasattr(self.data, 'columns') else [self.data.name]
        
        original_missing = self.data.isnull().sum().sum()
        
        if method == 'auto':
            # Auto-select method based on data characteristics
            for col in columns:
                if col in self.data.columns:
                    missing_pct = self.data[col].isnull().sum() / len(self.data)
                    if missing_pct > 0.5:
                        self.data = self.data.dropna(subset=[col])
                        self.cleaning_log.append(f"Dropped rows with missing {col} (>50% missing)")
                    elif self.data[col].dtype in ['object', 'category']:
                        self.data[col] = self.data[col].fillna(self.data[col].mode().iloc[0] if not self.data[col].mode().empty else 'Unknown')
                        self.cleaning_log.append(f"Filled {col} with mode")
                    else:
                        self.data[col] = self.data[col].fillna(self.data[col].median())
                        self.cleaning_log.append(f"Filled {col} with median")
        
        elif method == 'drop':
            self.data = self.data.dropna(subset=columns)
            self.cleaning_log.append(f"Dropped rows with missing values in {columns}")
        
        elif method == 'fill':
            if fill_value is None:
                raise ValueError("fill_value must be provided when method='fill'")
            self.data[columns] = self.data[columns].fillna(fill_value)
            self.cleaning_log.append(f"Filled missing values in {columns} with {fill_value}")
        
        elif method == 'interpolate':
            self.data[columns] = self.data[columns].interpolate()
            self.cleaning_log.append(f"Interpolated missing values in {columns}")
        
        new_missing = self.data.isnull().sum().sum()
        logger.info(f"Missing values reduced from {original_missing} to {new_missing}")
        
        return self
    
    def remove_duplicates(self, subset: Optional[List[str]] = None, keep: str = 'first') -> 'DataCleaner':
        """
        Remove duplicate rows.
        
        Args:
            subset: Columns to consider for duplicates
            keep: Which duplicates to keep ('first', 'last', False)
            
        Returns:
            self for method chaining
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        original_count = len(self.data)
        self.data = self.data.drop_duplicates(subset=subset, keep=keep)
        removed_count = original_count - len(self.data)
        
        self.cleaning_log.append(f"Removed {removed_count} duplicate rows")
        logger.info(f"Removed {removed_count} duplicate rows")
        
        return self
    
    def detect_outliers(self, 
                       method: str = 'iqr',
                       columns: Optional[List[str]] = None,
                       threshold: float = 1.5) -> Dict[str, List[int]]:
        """
        Detect outliers using various methods.
        
        Args:
            method: Method to detect outliers ('iqr', 'zscore', 'modified_zscore')
            columns: Columns to check for outliers
            threshold: Threshold for outlier detection
            
        Returns:
            Dictionary with outlier indices by column
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if columns is None:
            columns = self._get_numeric_columns()
        
        outliers = {}
        
        for col in columns:
            if col not in self.data.columns:
                continue
                
            data_col = self.data[col].dropna()
            
            if method == 'iqr':
                Q1 = data_col.quantile(0.25)
                Q3 = data_col.quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                outlier_mask = (self.data[col] < lower_bound) | (self.data[col] > upper_bound)
            
            elif method == 'zscore':
                z_scores = np.abs(stats.zscore(data_col))
                outlier_mask = z_scores > threshold
            
            elif method == 'modified_zscore':
                median = np.median(data_col)
                mad = np.median(np.abs(data_col - median))
                modified_z_scores = 0.6745 * (data_col - median) / mad
                outlier_mask = np.abs(modified_z_scores) > threshold
            
            outliers[col] = self.data[outlier_mask].index.tolist()
        
        return outliers
    
    def handle_outliers(self, 
                       method: str = 'iqr',
                       action: str = 'remove',
                       columns: Optional[List[str]] = None,
                       threshold: float = 1.5,
                       replacement_value: Any = None) -> 'DataCleaner':
        """
        Handle outliers using various methods.
        
        Args:
            method: Method to detect outliers
            action: Action to take ('remove', 'cap', 'replace')
            columns: Columns to process
            threshold: Threshold for outlier detection
            replacement_value: Value to replace outliers with
            
        Returns:
            self for method chaining
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        outliers = self.detect_outliers(method=method, columns=columns, threshold=threshold)
        
        if action == 'remove':
            outlier_indices = set()
            for col_outliers in outliers.values():
                outlier_indices.update(col_outliers)
            
            original_count = len(self.data)
            self.data = self.data.drop(index=list(outlier_indices))
            removed_count = original_count - len(self.data)
            
            self.cleaning_log.append(f"Removed {removed_count} rows with outliers")
            logger.info(f"Removed {removed_count} rows with outliers")
        
        elif action == 'cap':
            for col, outlier_indices in outliers.items():
                if not outlier_indices:
                    continue
                
                data_col = self.data[col].dropna()
                Q1 = data_col.quantile(0.25)
                Q3 = data_col.quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                
                self.data.loc[self.data[col] < lower_bound, col] = lower_bound
                self.data.loc[self.data[col] > upper_bound, col] = upper_bound
                
                self.cleaning_log.append(f"Capped outliers in {col}")
        
        elif action == 'replace':
            if replacement_value is None:
                raise ValueError("replacement_value must be provided when action='replace'")
            
            for col, outlier_indices in outliers.items():
                self.data.loc[outlier_indices, col] = replacement_value
                self.cleaning_log.append(f"Replaced outliers in {col} with {replacement_value}")
        
        return self
    
    def convert_data_types(self, 
                          type_mapping: Optional[Dict[str, str]] = None,
                          auto_convert: bool = True) -> 'DataCleaner':
        """
        Convert data types of columns.
        
        Args:
            type_mapping: Dictionary mapping column names to target types
            auto_convert: Whether to automatically convert obvious types
            
        Returns:
            self for method chaining
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if auto_convert:
            # Auto-convert obvious types
            for col in self.data.columns:
                if self.data[col].dtype == 'object':
                    # Try to convert to numeric
                    try:
                        self.data[col] = pd.to_numeric(self.data[col], errors='ignore')
                    except:
                        pass
                    
                    # Try to convert to datetime
                    if self.data[col].dtype == 'object':
                        try:
                            self.data[col] = pd.to_datetime(self.data[col], errors='ignore')
                        except:
                            pass
            
            self.cleaning_log.append("Auto-converted data types")
        
        if type_mapping:
            for col, target_type in type_mapping.items():
                if col in self.data.columns:
                    try:
                        if target_type == 'category':
                            self.data[col] = self.data[col].astype('category')
                        elif target_type == 'datetime':
                            self.data[col] = pd.to_datetime(self.data[col])
                        else:
                            self.data[col] = self.data[col].astype(target_type)
                        
                        self.cleaning_log.append(f"Converted {col} to {target_type}")
                    except Exception as e:
                        logger.warning(f"Failed to convert {col} to {target_type}: {e}")
        
        return self
    
    def validate_data(self, 
                     rules: Optional[Dict[str, Any]] = None,
                     strict: bool = False) -> Dict[str, Any]:
        """
        Validate data against specified rules.
        
        Args:
            rules: Dictionary of validation rules
            strict: Whether to raise errors on validation failures
            
        Returns:
            Dictionary with validation results
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        validation_results = {
            "passed": True,
            "errors": [],
            "warnings": [],
            "summary": {}
        }
        
        # Basic validations
        if len(self.data) == 0:
            validation_results["errors"].append("Data is empty")
            validation_results["passed"] = False
        
        # Check for completely empty columns
        empty_cols = self.data.columns[self.data.isnull().all()].tolist()
        if empty_cols:
            validation_results["warnings"].append(f"Completely empty columns: {empty_cols}")
        
        # Custom rules validation
        if rules:
            for rule_name, rule_config in rules.items():
                try:
                    if rule_config["type"] == "range":
                        col = rule_config["column"]
                        min_val = rule_config.get("min")
                        max_val = rule_config.get("max")
                        
                        if min_val is not None:
                            violations = (self.data[col] < min_val).sum()
                            if violations > 0:
                                validation_results["errors"].append(
                                    f"Rule '{rule_name}': {violations} values below minimum {min_val} in {col}"
                                )
                                validation_results["passed"] = False
                        
                        if max_val is not None:
                            violations = (self.data[col] > max_val).sum()
                            if violations > 0:
                                validation_results["errors"].append(
                                    f"Rule '{rule_name}': {violations} values above maximum {max_val} in {col}"
                                )
                                validation_results["passed"] = False
                    
                    elif rule_config["type"] == "unique":
                        col = rule_config["column"]
                        if self.data[col].nunique() != len(self.data):
                            validation_results["warnings"].append(
                                f"Rule '{rule_name}': Column {col} is not unique"
                            )
                
                except Exception as e:
                    validation_results["errors"].append(f"Rule '{rule_name}' validation failed: {e}")
                    validation_results["passed"] = False
        
        if strict and not validation_results["passed"]:
            raise ValueError(f"Data validation failed: {validation_results['errors']}")
        
        return validation_results
    
    def get_cleaning_summary(self) -> Dict[str, Any]:
        """
        Get summary of all cleaning operations performed.
        
        Returns:
            Dictionary with cleaning summary
        """
        return {
            "original_shape": self.original_data.shape if self.original_data is not None else None,
            "current_shape": self.data.shape if self.data is not None else None,
            "cleaning_operations": self.cleaning_log,
            "data_info": self.get_info() if self.data is not None else None
        }
    
    def reset(self) -> 'DataCleaner':
        """
        Reset to original data.
        
        Returns:
            self for method chaining
        """
        if self.original_data is not None:
            self.data = self.original_data.copy()
            self.cleaning_log = []
            logger.info("Data reset to original state")
        return self
    
    def save_cleaned_data(self, filepath: str, format: str = 'csv') -> 'DataCleaner':
        """
        Save cleaned data to file.
        
        Args:
            filepath: Path to save the file
            format: File format ('csv', 'excel', 'json', 'parquet')
            
        Returns:
            self for method chaining
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if format == 'csv':
            self.data.to_csv(filepath, index=False)
        elif format == 'excel':
            self.data.to_excel(filepath, index=False)
        elif format == 'json':
            self.data.to_json(filepath, orient='records')
        elif format == 'parquet':
            self.data.to_parquet(filepath, index=False)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        self.cleaning_log.append(f"Data saved to {filepath} in {format} format")
        logger.info(f"Data saved to {filepath}")
        
        return self
