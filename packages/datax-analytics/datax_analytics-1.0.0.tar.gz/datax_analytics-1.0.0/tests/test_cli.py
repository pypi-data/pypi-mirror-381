"""
Tests for the DataX CLI module.
"""

import pytest
import pandas as pd
import numpy as np
import tempfile
import os
import sys
from unittest.mock import patch, MagicMock
from datax.cli import DataXCLI, main
import argparse


class TestDataXCLI:
    """Test cases for DataXCLI class."""
    
    def test_init(self):
        """Test CLI initialization."""
        cli = DataXCLI()
        assert cli.parser is not None
        assert cli.data is None
        assert cli.cleaner is None
        assert cli.analyzer is None
        assert cli.visualizer is None
    
    def test_create_parser(self):
        """Test argument parser creation."""
        cli = DataXCLI()
        parser = cli._create_parser()
        
        assert isinstance(parser, argparse.ArgumentParser)
        assert parser.prog == 'DataX - Advanced Data Analytics Package'
    
    def test_load_data_csv(self, temp_file):
        """Test loading CSV data."""
        cli = DataXCLI()
        result = cli.load_data(temp_file)
        
        assert result is True
        assert cli.data is not None
        assert cli.cleaner is not None
        assert cli.analyzer is not None
        assert cli.visualizer is not None
        assert cli.data.shape == (3, 3)
    
    def test_load_data_excel(self, sample_dataframe, temp_file):
        """Test loading Excel data."""
        # Create Excel file
        excel_path = temp_file.replace('.csv', '.xlsx')
        sample_dataframe.to_excel(excel_path, index=False)
        
        cli = DataXCLI()
        result = cli.load_data(excel_path)
        
        assert result is True
        assert cli.data is not None
        
        # Cleanup
        if os.path.exists(excel_path):
            os.unlink(excel_path)
    
    def test_load_data_json(self, sample_dataframe, temp_file):
        """Test loading JSON data."""
        # Create JSON file
        json_path = temp_file.replace('.csv', '.json')
        sample_dataframe.to_json(json_path, orient='records')
        
        cli = DataXCLI()
        result = cli.load_data(json_path)
        
        assert result is True
        assert cli.data is not None
        
        # Cleanup
        if os.path.exists(json_path):
            os.unlink(json_path)
    
    def test_load_data_parquet(self, sample_dataframe, temp_file):
        """Test loading Parquet data."""
        # Create Parquet file
        parquet_path = temp_file.replace('.csv', '.parquet')
        sample_dataframe.to_parquet(parquet_path, index=False)
        
        cli = DataXCLI()
        result = cli.load_data(parquet_path)
        
        assert result is True
        assert cli.data is not None
        
        # Cleanup
        if os.path.exists(parquet_path):
            os.unlink(parquet_path)
    
    def test_load_data_file_not_found(self):
        """Test loading non-existent file."""
        cli = DataXCLI()
        result = cli.load_data('non_existent_file.csv')
        
        assert result is False
    
    def test_load_data_unsupported_format(self, temp_file):
        """Test loading unsupported file format."""
        # Create unsupported file
        unsupported_path = temp_file.replace('.csv', '.txt')
        with open(unsupported_path, 'w') as f:
            f.write('some text')
        
        cli = DataXCLI()
        result = cli.load_data(unsupported_path)
        
        assert result is False
        
        # Cleanup
        if os.path.exists(unsupported_path):
            os.unlink(unsupported_path)
    
    def test_show_data_info(self, sample_dataframe):
        """Test showing data information."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.cleaner = MagicMock()
        cli.cleaner.get_info.return_value = {
            'shape': sample_dataframe.shape,
            'columns': list(sample_dataframe.columns),
            'dtypes': sample_dataframe.dtypes.to_dict(),
            'memory_usage': sample_dataframe.memory_usage(deep=True).sum(),
            'missing_values': {'total_missing': 0, 'columns_with_missing': {}},
            'duplicates': 0,
            'numeric_columns': ['numeric_col', 'missing_col'],
            'categorical_columns': ['categorical_col'],
            'datetime_columns': ['date_col']
        }
        
        # Should not raise an exception
        cli.show_data_info()
    
    def test_show_data_info_no_data(self):
        """Test showing data info when no data is loaded."""
        cli = DataXCLI()
        
        # Should not raise an exception
        cli.show_data_info()
    
    def test_clean_data_auto_missing(self, sample_dataframe):
        """Test data cleaning with auto missing value handling."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.cleaner = MagicMock()
        cli.analyzer = MagicMock()
        cli.visualizer = MagicMock()
        
        # Mock cleaner methods
        cli.cleaner.handle_missing_values.return_value = cli.cleaner
        cli.cleaner.remove_duplicates.return_value = cli.cleaner
        cli.cleaner.handle_outliers.return_value = cli.cleaner
        cli.cleaner.convert_data_types.return_value = cli.cleaner
        cli.cleaner.validate_data.return_value = {'passed': True}
        cli.cleaner.get_cleaning_summary.return_value = {
            'original_shape': sample_dataframe.shape,
            'current_shape': sample_dataframe.shape,
            'cleaning_operations': ['test operation']
        }
        
        # Mock args
        args = MagicMock()
        args.missing = 'auto'
        args.fill_value = None
        args.remove_duplicates = False
        args.outliers = None
        args.outlier_method = 'iqr'
        args.outlier_threshold = 1.5
        args.convert_types = False
        args.validate = False
        
        result = cli.clean_data(args)
        
        assert result is True
        cli.cleaner.handle_missing_values.assert_called_once()
    
    def test_clean_data_remove_duplicates(self, sample_dataframe):
        """Test data cleaning with duplicate removal."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.cleaner = MagicMock()
        cli.analyzer = MagicMock()
        cli.visualizer = MagicMock()
        
        # Mock cleaner methods
        cli.cleaner.remove_duplicates.return_value = cli.cleaner
        cli.cleaner.get_cleaning_summary.return_value = {
            'original_shape': sample_dataframe.shape,
            'current_shape': sample_dataframe.shape,
            'cleaning_operations': ['test operation']
        }
        
        # Mock args
        args = MagicMock()
        args.missing = None
        args.fill_value = None
        args.remove_duplicates = True
        args.outliers = None
        args.outlier_method = 'iqr'
        args.outlier_threshold = 1.5
        args.convert_types = False
        args.validate = False
        
        result = cli.clean_data(args)
        
        assert result is True
        cli.cleaner.remove_duplicates.assert_called_once()
    
    def test_clean_data_handle_outliers(self, sample_dataframe):
        """Test data cleaning with outlier handling."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.cleaner = MagicMock()
        cli.analyzer = MagicMock()
        cli.visualizer = MagicMock()
        
        # Mock cleaner methods
        cli.cleaner.handle_outliers.return_value = cli.cleaner
        cli.cleaner.get_cleaning_summary.return_value = {
            'original_shape': sample_dataframe.shape,
            'current_shape': sample_dataframe.shape,
            'cleaning_operations': ['test operation']
        }
        
        # Mock args
        args = MagicMock()
        args.missing = None
        args.fill_value = None
        args.remove_duplicates = False
        args.outliers = 'remove'
        args.outlier_method = 'iqr'
        args.outlier_threshold = 1.5
        args.convert_types = False
        args.validate = False
        
        result = cli.clean_data(args)
        
        assert result is True
        cli.cleaner.handle_outliers.assert_called_once()
    
    def test_clean_data_convert_types(self, sample_dataframe):
        """Test data cleaning with type conversion."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.cleaner = MagicMock()
        cli.analyzer = MagicMock()
        cli.visualizer = MagicMock()
        
        # Mock cleaner methods
        cli.cleaner.convert_data_types.return_value = cli.cleaner
        cli.cleaner.get_cleaning_summary.return_value = {
            'original_shape': sample_dataframe.shape,
            'current_shape': sample_dataframe.shape,
            'cleaning_operations': ['test operation']
        }
        
        # Mock args
        args = MagicMock()
        args.missing = None
        args.fill_value = None
        args.remove_duplicates = False
        args.outliers = None
        args.outlier_method = 'iqr'
        args.outlier_threshold = 1.5
        args.convert_types = True
        args.validate = False
        
        result = cli.clean_data(args)
        
        assert result is True
        cli.cleaner.convert_data_types.assert_called_once()
    
    def test_clean_data_validate(self, sample_dataframe):
        """Test data cleaning with validation."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.cleaner = MagicMock()
        cli.analyzer = MagicMock()
        cli.visualizer = MagicMock()
        
        # Mock cleaner methods
        cli.cleaner.validate_data.return_value = {'passed': True}
        cli.cleaner.get_cleaning_summary.return_value = {
            'original_shape': sample_dataframe.shape,
            'current_shape': sample_dataframe.shape,
            'cleaning_operations': ['test operation']
        }
        
        # Mock args
        args = MagicMock()
        args.missing = None
        args.fill_value = None
        args.remove_duplicates = False
        args.outliers = None
        args.outlier_method = 'iqr'
        args.outlier_threshold = 1.5
        args.convert_types = False
        args.validate = True
        
        result = cli.clean_data(args)
        
        assert result is True
        cli.cleaner.validate_data.assert_called_once()
    
    def test_clean_data_no_data(self):
        """Test data cleaning when no data is loaded."""
        cli = DataXCLI()
        args = MagicMock()
        
        result = cli.clean_data(args)
        
        assert result is False
    
    def test_perform_statistics_descriptive(self, sample_dataframe):
        """Test performing descriptive statistics."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.analyzer = MagicMock()
        
        # Mock analyzer methods
        cli.analyzer.get_descriptive_stats.return_value = {
            'numeric_col': {'count': 100, 'mean': 50, 'std': 10}
        }
        cli.analyzer.get_correlation_matrix.return_value = {
            'correlation_matrix': {},
            'strong_correlations': []
        }
        
        # Mock args
        args = MagicMock()
        args.descriptive = True
        args.correlation = False
        args.hypothesis = None
        args.regression = None
        args.anova = None
        args.normality = None
        args.export_results = None
        
        result = cli.perform_statistics(args)
        
        assert result is True
        cli.analyzer.get_descriptive_stats.assert_called_once()
    
    def test_perform_statistics_correlation(self, sample_dataframe):
        """Test performing correlation analysis."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.analyzer = MagicMock()
        
        # Mock analyzer methods
        cli.analyzer.get_correlation_matrix.return_value = {
            'correlation_matrix': {},
            'strong_correlations': []
        }
        
        # Mock args
        args = MagicMock()
        args.descriptive = False
        args.correlation = True
        args.hypothesis = None
        args.regression = None
        args.anova = None
        args.normality = None
        args.export_results = None
        
        result = cli.perform_statistics(args)
        
        assert result is True
        cli.analyzer.get_correlation_matrix.assert_called_once()
    
    def test_perform_statistics_export_results(self, sample_dataframe, temp_file):
        """Test performing statistics with result export."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.analyzer = MagicMock()
        
        # Mock analyzer methods
        cli.analyzer.get_descriptive_stats.return_value = {
            'numeric_col': {'count': 100, 'mean': 50, 'std': 10}
        }
        cli.analyzer.export_results.return_value = cli.analyzer
        
        # Mock args
        args = MagicMock()
        args.descriptive = True
        args.correlation = False
        args.hypothesis = None
        args.regression = None
        args.anova = None
        args.normality = None
        args.export_results = temp_file.replace('.csv', '_results.json')
        
        result = cli.perform_statistics(args)
        
        assert result is True
        cli.analyzer.export_results.assert_called_once()
    
    def test_perform_statistics_no_data(self):
        """Test performing statistics when no data is loaded."""
        cli = DataXCLI()
        args = MagicMock()
        
        result = cli.perform_statistics(args)
        
        assert result is False
    
    def test_create_visualizations_distributions(self, sample_dataframe):
        """Test creating distribution visualizations."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.visualizer = MagicMock()
        
        # Mock visualizer methods
        cli.visualizer.set_style.return_value = cli.visualizer
        cli.visualizer.plot_multiple_distributions.return_value = MagicMock()
        cli.visualizer.show_all_plots.return_value = None
        
        # Mock args
        args = MagicMock()
        args.distributions = True
        args.correlation_heatmap = False
        args.scatter_matrix = False
        args.time_series = None
        args.categorical = None
        args.interactive = False
        args.style = 'default'
        args.save_plots = None
        
        result = cli.create_visualizations(args)
        
        assert result is True
        cli.visualizer.plot_multiple_distributions.assert_called_once()
    
    def test_create_visualizations_correlation_heatmap(self, sample_dataframe):
        """Test creating correlation heatmap."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.visualizer = MagicMock()
        
        # Mock visualizer methods
        cli.visualizer.set_style.return_value = cli.visualizer
        cli.visualizer.plot_correlation_heatmap.return_value = MagicMock()
        cli.visualizer.show_all_plots.return_value = None
        
        # Mock args
        args = MagicMock()
        args.distributions = False
        args.correlation_heatmap = True
        args.scatter_matrix = False
        args.time_series = None
        args.categorical = None
        args.interactive = False
        args.style = 'default'
        args.save_plots = None
        
        result = cli.create_visualizations(args)
        
        assert result is True
        cli.visualizer.plot_correlation_heatmap.assert_called_once()
    
    def test_create_visualizations_scatter_matrix(self, sample_dataframe):
        """Test creating scatter matrix."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.visualizer = MagicMock()
        
        # Mock visualizer methods
        cli.visualizer.set_style.return_value = cli.visualizer
        cli.visualizer.plot_scatter_matrix.return_value = MagicMock()
        cli.visualizer.show_all_plots.return_value = None
        
        # Mock args
        args = MagicMock()
        args.distributions = False
        args.correlation_heatmap = False
        args.scatter_matrix = True
        args.time_series = None
        args.categorical = None
        args.interactive = False
        args.style = 'default'
        args.save_plots = None
        
        result = cli.create_visualizations(args)
        
        assert result is True
        cli.visualizer.plot_scatter_matrix.assert_called_once()
    
    def test_create_visualizations_save_plots(self, sample_dataframe, temp_dir):
        """Test creating visualizations with plot saving."""
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.visualizer = MagicMock()
        
        # Mock visualizer methods
        cli.visualizer.set_style.return_value = cli.visualizer
        cli.visualizer.plot_multiple_distributions.return_value = MagicMock()
        cli.visualizer.figures = [MagicMock(), MagicMock()]
        cli.visualizer.save_plot.return_value = cli.visualizer
        cli.visualizer.show_all_plots.return_value = None
        
        # Mock args
        args = MagicMock()
        args.distributions = True
        args.correlation_heatmap = False
        args.scatter_matrix = False
        args.time_series = None
        args.categorical = None
        args.interactive = False
        args.style = 'default'
        args.save_plots = temp_dir
        
        result = cli.create_visualizations(args)
        
        assert result is True
        assert cli.visualizer.save_plot.call_count == 2
    
    def test_create_visualizations_no_data(self):
        """Test creating visualizations when no data is loaded."""
        cli = DataXCLI()
        args = MagicMock()
        
        result = cli.create_visualizations(args)
        
        assert result is False
    
    @patch('builtins.input')
    def test_interactive_mode_quit(self, mock_input):
        """Test interactive mode quit command."""
        mock_input.side_effect = ['quit']
        
        cli = DataXCLI()
        args = MagicMock()
        args.file = None
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    @patch('builtins.input')
    def test_interactive_mode_help(self, mock_input):
        """Test interactive mode help command."""
        mock_input.side_effect = ['help', 'quit']
        
        cli = DataXCLI()
        args = MagicMock()
        args.file = None
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    @patch('builtins.input')
    def test_interactive_mode_load(self, mock_input, temp_file):
        """Test interactive mode load command."""
        mock_input.side_effect = [f'load {temp_file}', 'quit']
        
        cli = DataXCLI()
        args = MagicMock()
        args.file = None
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    @patch('builtins.input')
    def test_interactive_mode_info(self, mock_input, sample_dataframe):
        """Test interactive mode info command."""
        mock_input.side_effect = ['info', 'quit']
        
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.cleaner = MagicMock()
        cli.cleaner.get_info.return_value = {
            'shape': sample_dataframe.shape,
            'columns': list(sample_dataframe.columns),
            'dtypes': sample_dataframe.dtypes.to_dict(),
            'memory_usage': sample_dataframe.memory_usage(deep=True).sum(),
            'missing_values': {'total_missing': 0, 'columns_with_missing': {}},
            'duplicates': 0,
            'numeric_columns': ['numeric_col', 'missing_col'],
            'categorical_columns': ['categorical_col'],
            'datetime_columns': ['date_col']
        }
        
        args = MagicMock()
        args.file = None
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    @patch('builtins.input')
    def test_interactive_mode_clean(self, mock_input, sample_dataframe):
        """Test interactive mode clean command."""
        mock_input.side_effect = ['clean', 'quit']
        
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.cleaner = MagicMock()
        cli.analyzer = MagicMock()
        cli.visualizer = MagicMock()
        
        # Mock cleaner methods
        cli.cleaner.handle_missing_values.return_value = cli.cleaner
        cli.cleaner.remove_duplicates.return_value = cli.cleaner
        
        args = MagicMock()
        args.file = None
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    @patch('builtins.input')
    def test_interactive_mode_stats(self, mock_input, sample_dataframe):
        """Test interactive mode stats command."""
        mock_input.side_effect = ['stats', 'quit']
        
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.analyzer = MagicMock()
        cli.analyzer.get_descriptive_stats.return_value = {
            'numeric_col': {'count': 100, 'mean': 50, 'std': 10}
        }
        
        args = MagicMock()
        args.file = None
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    @patch('builtins.input')
    def test_interactive_mode_viz(self, mock_input, sample_dataframe):
        """Test interactive mode viz command."""
        mock_input.side_effect = ['viz', 'quit']
        
        cli = DataXCLI()
        cli.data = sample_dataframe
        cli.visualizer = MagicMock()
        cli.visualizer.plot_multiple_distributions.return_value = MagicMock()
        cli.visualizer.show_all_plots.return_value = None
        
        args = MagicMock()
        args.file = None
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    @patch('builtins.input')
    def test_interactive_mode_unknown_command(self, mock_input):
        """Test interactive mode unknown command."""
        mock_input.side_effect = ['unknown_command', 'quit']
        
        cli = DataXCLI()
        args = MagicMock()
        args.file = None
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    def test_interactive_mode_with_file(self, temp_file):
        """Test interactive mode with initial file."""
        cli = DataXCLI()
        args = MagicMock()
        args.file = temp_file
        
        # Should not raise an exception
        cli.interactive_mode(args)
    
    def test_run_no_command(self):
        """Test running CLI with no command."""
        cli = DataXCLI()
        result = cli.run(['--help'])
        
        assert result == 1
    
    def test_run_load_command(self, temp_file):
        """Test running load command."""
        cli = DataXCLI()
        result = cli.run(['load', temp_file, 'info'])
        
        assert result == 0
    
    def test_run_load_command_fail(self):
        """Test running load command with non-existent file."""
        cli = DataXCLI()
        result = cli.run(['load', 'non_existent_file.csv', 'info'])
        
        assert result == 1
    
    def test_run_clean_command_no_data(self):
        """Test running clean command with no data."""
        cli = DataXCLI()
        result = cli.run(['clean', '--missing', 'auto'])
        
        assert result == 1
    
    def test_run_stats_command_no_data(self):
        """Test running stats command with no data."""
        cli = DataXCLI()
        result = cli.run(['stats', '--descriptive'])
        
        assert result == 1
    
    def test_run_viz_command_no_data(self):
        """Test running viz command with no data."""
        cli = DataXCLI()
        result = cli.run(['viz', '--distributions'])
        
        assert result == 1
    
    def test_run_interactive_command(self):
        """Test running interactive command."""
        cli = DataXCLI()
        result = cli.run(['interactive'])
        
        assert result == 0
    
    def test_run_batch_command(self):
        """Test running batch command."""
        cli = DataXCLI()
        result = cli.run(['batch', 'config.json'])
        
        assert result == 1  # Not implemented yet
    
    def test_run_verbose(self, temp_file):
        """Test running with verbose flag."""
        cli = DataXCLI()
        result = cli.run(['--verbose', 'load', temp_file, 'info'])
        
        assert result == 0
    
    def test_run_version(self):
        """Test running with version flag."""
        cli = DataXCLI()
        result = cli.run(['--version'])
        
        assert result == 0
    
    def test_run_exception_handling(self):
        """Test exception handling in run method."""
        cli = DataXCLI()
        
        # Mock parser to raise exception
        with patch.object(cli.parser, 'parse_args', side_effect=Exception('Test error')):
            result = cli.run(['load', 'test.csv'])
            
            assert result == 1


def test_main_function():
    """Test main function entry point."""
    # Should not raise an exception
    with patch('sys.argv', ['datax', '--help']):
        with patch('datax.cli.DataXCLI') as mock_cli:
            mock_instance = MagicMock()
            mock_instance.run.return_value = 0
            mock_cli.return_value = mock_instance
            
            main()
            
            mock_instance.run.assert_called_once()
