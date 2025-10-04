"""
Statistical Analysis Module for DataX Package

This module provides comprehensive statistical analysis functionality including:
- Descriptive statistics
- Inferential statistics
- Correlation analysis
- Hypothesis testing
- Advanced statistical modeling
- Statistical significance testing
"""

import pandas as pd
import numpy as np
from typing import Union, List, Dict, Any, Optional, Tuple
import warnings
from scipy import stats
from scipy.stats import chi2_contingency, fisher_exact, mannwhitneyu, kruskal
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataAnalyzer:
    """
    Advanced statistical analysis class with comprehensive statistical methods.
    
    This class provides a wide range of statistical operations including
    descriptive statistics, inferential statistics, correlation analysis,
    hypothesis testing, and advanced statistical modeling.
    """
    
    def __init__(self, data: Union[pd.DataFrame, pd.Series] = None):
        """
        Initialize DataAnalyzer with optional data.
        
        Args:
            data: pandas DataFrame or Series to analyze
        """
        self.data = data.copy() if data is not None else None
        self.analysis_results = {}
        
    def load_data(self, data: Union[pd.DataFrame, pd.Series]) -> 'DataAnalyzer':
        """
        Load data into the analyzer.
        
        Args:
            data: pandas DataFrame or Series
            
        Returns:
            self for method chaining
        """
        self.data = data.copy()
        self.analysis_results = {}
        logger.info(f"Data loaded for analysis: {data.shape}")
        return self
    
    def get_descriptive_stats(self, 
                             columns: Optional[List[str]] = None,
                             include_all: bool = True) -> Dict[str, Any]:
        """
        Get comprehensive descriptive statistics.
        
        Args:
            columns: Specific columns to analyze
            include_all: Whether to include all statistical measures
            
        Returns:
            Dictionary with descriptive statistics
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if columns is None:
            if isinstance(self.data, pd.Series):
                columns = [self.data.name] if self.data.name else ['series']
                data_to_analyze = pd.DataFrame({columns[0]: self.data})
            else:
                columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
                data_to_analyze = self.data[columns]
        else:
            data_to_analyze = self.data[columns]
        
        if data_to_analyze.empty:
            return {"error": "No numeric columns found"}
        
        stats_dict = {}
        
        for col in columns:
            if col not in data_to_analyze.columns:
                continue
                
            series = data_to_analyze[col].dropna()
            
            if len(series) == 0:
                continue
            
            col_stats = {
                "count": len(series),
                "mean": series.mean(),
                "median": series.median(),
                "mode": series.mode().iloc[0] if not series.mode().empty else None,
                "std": series.std(),
                "var": series.var(),
                "min": series.min(),
                "max": series.max(),
                "range": series.max() - series.min(),
                "q25": series.quantile(0.25),
                "q75": series.quantile(0.75),
                "iqr": series.quantile(0.75) - series.quantile(0.25),
                "skewness": series.skew(),
                "kurtosis": series.kurtosis(),
                "missing_count": data_to_analyze[col].isnull().sum(),
                "missing_percentage": (data_to_analyze[col].isnull().sum() / len(data_to_analyze)) * 100
            }
            
            if include_all:
                col_stats.update({
                    "sum": series.sum(),
                    "sem": series.sem(),  # Standard error of mean
                    "mad": (series - series.mean()).abs().mean(),  # Mean absolute deviation
                    "cv": series.std() / series.mean() if series.mean() != 0 else np.inf,  # Coefficient of variation
                    "z_scores": stats.zscore(series).tolist(),
                    "percentiles": {
                        "p10": series.quantile(0.10),
                        "p20": series.quantile(0.20),
                        "p30": series.quantile(0.30),
                        "p40": series.quantile(0.40),
                        "p50": series.quantile(0.50),
                        "p60": series.quantile(0.60),
                        "p70": series.quantile(0.70),
                        "p80": series.quantile(0.80),
                        "p90": series.quantile(0.90),
                        "p95": series.quantile(0.95),
                        "p99": series.quantile(0.99)
                    }
                })
            
            stats_dict[col] = col_stats
        
        self.analysis_results["descriptive_stats"] = stats_dict
        return stats_dict
    
    def get_correlation_matrix(self, 
                              method: str = 'pearson',
                              columns: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Calculate correlation matrix.
        
        Args:
            method: Correlation method ('pearson', 'spearman', 'kendall')
            columns: Specific columns to analyze
            
        Returns:
            Dictionary with correlation results
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if columns is None:
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
            if len(numeric_cols) < 2:
                return {"error": "Need at least 2 numeric columns for correlation"}
            columns = numeric_cols
        
        data_subset = self.data[columns].dropna()
        
        if len(data_subset) < 2:
            return {"error": "Insufficient data for correlation analysis"}
        
        correlation_matrix = data_subset.corr(method=method)
        
        # Find strong correlations
        strong_correlations = []
        for i in range(len(correlation_matrix.columns)):
            for j in range(i+1, len(correlation_matrix.columns)):
                corr_value = correlation_matrix.iloc[i, j]
                if abs(corr_value) > 0.7:  # Strong correlation threshold
                    strong_correlations.append({
                        "var1": correlation_matrix.columns[i],
                        "var2": correlation_matrix.columns[j],
                        "correlation": corr_value,
                        "strength": "strong" if abs(corr_value) > 0.8 else "moderate"
                    })
        
        result = {
            "correlation_matrix": correlation_matrix.to_dict(),
            "strong_correlations": strong_correlations,
            "method": method,
            "data_points": len(data_subset)
        }
        
        self.analysis_results["correlation"] = result
        return result
    
    def hypothesis_test(self, 
                       test_type: str,
                       **kwargs) -> Dict[str, Any]:
        """
        Perform various hypothesis tests.
        
        Args:
            test_type: Type of test ('ttest', 'chi2', 'mannwhitney', 'kruskal', 'normality')
            **kwargs: Test-specific parameters
            
        Returns:
            Dictionary with test results
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if test_type == 'ttest':
            return self._perform_ttest(**kwargs)
        elif test_type == 'chi2':
            return self._perform_chi2_test(**kwargs)
        elif test_type == 'mannwhitney':
            return self._perform_mannwhitney_test(**kwargs)
        elif test_type == 'kruskal':
            return self._perform_kruskal_test(**kwargs)
        elif test_type == 'normality':
            return self._perform_normality_test(**kwargs)
        else:
            raise ValueError(f"Unsupported test type: {test_type}")
    
    def _perform_ttest(self, 
                      column1: str,
                      column2: Optional[str] = None,
                      alternative: str = 'two-sided',
                      mu: float = 0) -> Dict[str, Any]:
        """Perform t-test."""
        if column2 is None:
            # One-sample t-test
            data1 = self.data[column1].dropna()
            statistic, p_value = stats.ttest_1samp(data1, mu)
            test_type = "one_sample"
        else:
            # Two-sample t-test
            data1 = self.data[column1].dropna()
            data2 = self.data[column2].dropna()
            statistic, p_value = stats.ttest_ind(data1, data2, alternative=alternative)
            test_type = "two_sample"
        
        result = {
            "test_type": test_type,
            "statistic": statistic,
            "p_value": p_value,
            "significant": p_value < 0.05,
            "alpha": 0.05,
            "columns": [column1] if column2 is None else [column1, column2]
        }
        
        self.analysis_results[f"ttest_{test_type}"] = result
        return result
    
    def _perform_chi2_test(self, 
                          column1: str,
                          column2: str) -> Dict[str, Any]:
        """Perform chi-square test of independence."""
        contingency_table = pd.crosstab(self.data[column1], self.data[column2])
        chi2, p_value, dof, expected = chi2_contingency(contingency_table)
        
        result = {
            "test_type": "chi2_independence",
            "chi2_statistic": chi2,
            "p_value": p_value,
            "degrees_of_freedom": dof,
            "significant": p_value < 0.05,
            "contingency_table": contingency_table.to_dict(),
            "expected_frequencies": expected.tolist(),
            "columns": [column1, column2]
        }
        
        self.analysis_results["chi2_test"] = result
        return result
    
    def _perform_mannwhitney_test(self, 
                                 column1: str,
                                 column2: str,
                                 alternative: str = 'two-sided') -> Dict[str, Any]:
        """Perform Mann-Whitney U test."""
        data1 = self.data[column1].dropna()
        data2 = self.data[column2].dropna()
        
        statistic, p_value = mannwhitneyu(data1, data2, alternative=alternative)
        
        result = {
            "test_type": "mannwhitney",
            "statistic": statistic,
            "p_value": p_value,
            "significant": p_value < 0.05,
            "columns": [column1, column2]
        }
        
        self.analysis_results["mannwhitney_test"] = result
        return result
    
    def _perform_kruskal_test(self, 
                             value_column: str,
                             group_column: str) -> Dict[str, Any]:
        """Perform Kruskal-Wallis test."""
        groups = []
        group_names = []
        
        for group in self.data[group_column].unique():
            group_data = self.data[self.data[group_column] == group][value_column].dropna()
            if len(group_data) > 0:
                groups.append(group_data)
                group_names.append(group)
        
        if len(groups) < 2:
            return {"error": "Need at least 2 groups for Kruskal-Wallis test"}
        
        statistic, p_value = kruskal(*groups)
        
        result = {
            "test_type": "kruskal_wallis",
            "statistic": statistic,
            "p_value": p_value,
            "significant": p_value < 0.05,
            "groups": group_names,
            "columns": [value_column, group_column]
        }
        
        self.analysis_results["kruskal_test"] = result
        return result
    
    def _perform_normality_test(self, 
                               column: str,
                               test: str = 'shapiro') -> Dict[str, Any]:
        """Perform normality test."""
        data = self.data[column].dropna()
        
        if test == 'shapiro':
            if len(data) > 5000:
                # Shapiro-Wilk is not reliable for large samples
                warnings.warn("Shapiro-Wilk test is not reliable for samples > 5000")
            statistic, p_value = stats.shapiro(data)
        elif test == 'kstest':
            statistic, p_value = stats.kstest(data, 'norm', args=(data.mean(), data.std()))
        elif test == 'jarque_bera':
            statistic, p_value = stats.jarque_bera(data)
        else:
            raise ValueError(f"Unsupported normality test: {test}")
        
        result = {
            "test_type": f"normality_{test}",
            "statistic": statistic,
            "p_value": p_value,
            "normal": p_value > 0.05,
            "column": column
        }
        
        self.analysis_results[f"normality_{test}"] = result
        return result
    
    def regression_analysis(self, 
                           target_column: str,
                           feature_columns: Optional[List[str]] = None,
                           method: str = 'linear') -> Dict[str, Any]:
        """
        Perform regression analysis.
        
        Args:
            target_column: Target variable column
            feature_columns: Feature columns (None for all numeric columns)
            method: Regression method ('linear')
            
        Returns:
            Dictionary with regression results
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if feature_columns is None:
            feature_columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
            if target_column in feature_columns:
                feature_columns.remove(target_column)
        
        if not feature_columns:
            return {"error": "No feature columns available"}
        
        # Prepare data
        X = self.data[feature_columns].dropna()
        y = self.data[target_column].dropna()
        
        # Align indices
        common_indices = X.index.intersection(y.index)
        X = X.loc[common_indices]
        y = y.loc[common_indices]
        
        if len(X) == 0:
            return {"error": "No common data points between features and target"}
        
        if method == 'linear':
            model = LinearRegression()
            model.fit(X, y)
            
            y_pred = model.predict(X)
            
            # Calculate metrics
            r2 = r2_score(y, y_pred)
            mse = mean_squared_error(y, y_pred)
            rmse = np.sqrt(mse)
            mae = mean_absolute_error(y, y_pred)
            
            # Feature importance (coefficients)
            feature_importance = dict(zip(feature_columns, model.coef_))
            
            result = {
                "method": "linear_regression",
                "r2_score": r2,
                "mse": mse,
                "rmse": rmse,
                "mae": mae,
                "intercept": model.intercept_,
                "coefficients": feature_importance,
                "feature_columns": feature_columns,
                "target_column": target_column,
                "n_samples": len(X),
                "predictions": y_pred.tolist()
            }
            
            self.analysis_results["regression"] = result
            return result
        
        else:
            raise ValueError(f"Unsupported regression method: {method}")
    
    def anova_analysis(self, 
                      value_column: str,
                      group_column: str) -> Dict[str, Any]:
        """
        Perform ANOVA analysis.
        
        Args:
            value_column: Numeric column to analyze
            group_column: Categorical column for grouping
            
        Returns:
            Dictionary with ANOVA results
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        groups = []
        group_names = []
        
        for group in self.data[group_column].unique():
            group_data = self.data[self.data[group_column] == group][value_column].dropna()
            if len(group_data) > 0:
                groups.append(group_data)
                group_names.append(group)
        
        if len(groups) < 2:
            return {"error": "Need at least 2 groups for ANOVA"}
        
        # Perform one-way ANOVA
        f_statistic, p_value = stats.f_oneway(*groups)
        
        # Calculate group statistics
        group_stats = {}
        for i, (group_name, group_data) in enumerate(zip(group_names, groups)):
            group_stats[group_name] = {
                "count": len(group_data),
                "mean": group_data.mean(),
                "std": group_data.std(),
                "min": group_data.min(),
                "max": group_data.max()
            }
        
        result = {
            "test_type": "one_way_anova",
            "f_statistic": f_statistic,
            "p_value": p_value,
            "significant": p_value < 0.05,
            "groups": group_names,
            "group_statistics": group_stats,
            "columns": [value_column, group_column]
        }
        
        self.analysis_results["anova"] = result
        return result
    
    def get_summary_report(self) -> Dict[str, Any]:
        """
        Get comprehensive summary report of all analyses.
        
        Returns:
            Dictionary with complete analysis summary
        """
        if self.data is None:
            return {"error": "No data loaded"}
        
        report = {
            "data_info": {
                "shape": self.data.shape,
                "columns": list(self.data.columns) if hasattr(self.data, 'columns') else [self.data.name],
                "numeric_columns": self.data.select_dtypes(include=[np.number]).columns.tolist() if hasattr(self.data, 'columns') else [],
                "categorical_columns": self.data.select_dtypes(include=['object', 'category']).columns.tolist() if hasattr(self.data, 'columns') else []
            },
            "analyses_performed": list(self.analysis_results.keys()),
            "results": self.analysis_results
        }
        
        return report
    
    def export_results(self, filepath: str, format: str = 'json') -> 'DataAnalyzer':
        """
        Export analysis results to file.
        
        Args:
            filepath: Path to save the file
            format: File format ('json', 'csv', 'excel')
            
        Returns:
            self for method chaining
        """
        if not self.analysis_results:
            logger.warning("No analysis results to export")
            return self
        
        if format == 'json':
            import json
            with open(filepath, 'w') as f:
                json.dump(self.analysis_results, f, indent=2, default=str)
        elif format == 'csv':
            # Export summary statistics as CSV
            if 'descriptive_stats' in self.analysis_results:
                stats_df = pd.DataFrame(self.analysis_results['descriptive_stats']).T
                stats_df.to_csv(filepath)
        elif format == 'excel':
            # Export to Excel with multiple sheets
            with pd.ExcelWriter(filepath) as writer:
                if 'descriptive_stats' in self.analysis_results:
                    stats_df = pd.DataFrame(self.analysis_results['descriptive_stats']).T
                    stats_df.to_excel(writer, sheet_name='Descriptive_Stats')
                
                if 'correlation' in self.analysis_results:
                    corr_df = pd.DataFrame(self.analysis_results['correlation']['correlation_matrix'])
                    corr_df.to_excel(writer, sheet_name='Correlation')
        
        logger.info(f"Analysis results exported to {filepath}")
        return self
