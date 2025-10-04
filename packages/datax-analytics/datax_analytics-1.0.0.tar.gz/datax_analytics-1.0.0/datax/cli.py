"""
Command Line Interface for DataX Package

This module provides a comprehensive CLI for the DataX package including:
- Data cleaning operations
- Statistical analysis
- Data visualization
- Batch processing
- Interactive mode
"""

import argparse
import sys
import os
import json
import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
import logging
from pathlib import Path

# Import DataX modules
from .cleaning import DataCleaner
from .stats import DataAnalyzer
from .viz import DataVisualizer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DataXCLI:
    """
    Command Line Interface for DataX package.
    
    Provides comprehensive CLI functionality for data cleaning, analysis, and visualization.
    """
    
    def __init__(self):
        """Initialize CLI."""
        self.parser = self._create_parser()
        self.data = None
        self.cleaner = None
        self.analyzer = None
        self.visualizer = None
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create argument parser with all commands."""
        parser = argparse.ArgumentParser(
            description='DataX - Advanced Data Analytics Package',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  # Load data and get info
  datax load data.csv info
  
  # Clean data with auto missing value handling
  datax load data.csv clean --missing auto
  
  # Perform statistical analysis
  datax load data.csv stats --descriptive --correlation
  
  # Create visualizations
  datax load data.csv viz --distributions --correlation-heatmap
  
  # Interactive mode
  datax interactive
            """
        )
        
        # Global arguments
        parser.add_argument('--version', action='version', version='DataX 1.0.0')
        parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
        parser.add_argument('--output', '-o', help='Output file path')
        parser.add_argument('--format', choices=['csv', 'excel', 'json', 'parquet'], 
                          default='csv', help='Output format')
        
        # Subcommands
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Load command
        load_parser = subparsers.add_parser('load', help='Load data from file')
        load_parser.add_argument('file', help='Data file path')
        load_parser.add_argument('action', nargs='?', choices=['info', 'clean', 'stats', 'viz'], 
                               help='Action to perform after loading')
        
        # Clean command
        clean_parser = subparsers.add_parser('clean', help='Data cleaning operations')
        clean_parser.add_argument('--missing', choices=['auto', 'drop', 'fill', 'interpolate'], 
                                default='auto', help='Missing value handling method')
        clean_parser.add_argument('--fill-value', help='Value to fill missing values with')
        clean_parser.add_argument('--remove-duplicates', action='store_true', 
                                help='Remove duplicate rows')
        clean_parser.add_argument('--outliers', choices=['remove', 'cap', 'replace'], 
                                help='Outlier handling method')
        clean_parser.add_argument('--outlier-method', choices=['iqr', 'zscore', 'modified_zscore'], 
                                default='iqr', help='Outlier detection method')
        clean_parser.add_argument('--outlier-threshold', type=float, default=1.5, 
                                help='Outlier detection threshold')
        clean_parser.add_argument('--convert-types', action='store_true', 
                                help='Auto-convert data types')
        clean_parser.add_argument('--validate', action='store_true', 
                                help='Validate data after cleaning')
        
        # Stats command
        stats_parser = subparsers.add_parser('stats', help='Statistical analysis')
        stats_parser.add_argument('--descriptive', action='store_true', 
                                help='Calculate descriptive statistics')
        stats_parser.add_argument('--correlation', action='store_true', 
                                help='Calculate correlation matrix')
        stats_parser.add_argument('--hypothesis', help='Perform hypothesis test')
        stats_parser.add_argument('--regression', help='Perform regression analysis')
        stats_parser.add_argument('--anova', help='Perform ANOVA analysis')
        stats_parser.add_argument('--normality', help='Test for normality')
        stats_parser.add_argument('--export-results', help='Export results to file')
        
        # Viz command
        viz_parser = subparsers.add_parser('viz', help='Data visualization')
        viz_parser.add_argument('--distributions', action='store_true', 
                              help='Plot distributions')
        viz_parser.add_argument('--correlation-heatmap', action='store_true', 
                              help='Plot correlation heatmap')
        viz_parser.add_argument('--scatter-matrix', action='store_true', 
                              help='Plot scatter matrix')
        viz_parser.add_argument('--time-series', help='Plot time series')
        viz_parser.add_argument('--categorical', help='Plot categorical analysis')
        viz_parser.add_argument('--interactive', action='store_true', 
                              help='Create interactive plots')
        viz_parser.add_argument('--style', choices=['default', 'dark', 'minimal', 'colorful'], 
                              default='default', help='Plot style')
        viz_parser.add_argument('--save-plots', help='Directory to save plots')
        
        # Interactive command
        interactive_parser = subparsers.add_parser('interactive', help='Start interactive mode')
        interactive_parser.add_argument('--file', help='Data file to load in interactive mode')
        
        # Batch command
        batch_parser = subparsers.add_parser('batch', help='Batch processing')
        batch_parser.add_argument('config', help='JSON configuration file for batch processing')
        
        return parser
    
    def load_data(self, filepath: str) -> bool:
        """
        Load data from file.
        
        Args:
            filepath: Path to data file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            filepath = Path(filepath)
            
            if not filepath.exists():
                logger.error(f"File not found: {filepath}")
                return False
            
            # Determine file format and load accordingly
            if filepath.suffix.lower() == '.csv':
                self.data = pd.read_csv(filepath)
            elif filepath.suffix.lower() in ['.xlsx', '.xls']:
                self.data = pd.read_excel(filepath)
            elif filepath.suffix.lower() == '.json':
                self.data = pd.read_json(filepath)
            elif filepath.suffix.lower() == '.parquet':
                self.data = pd.read_parquet(filepath)
            else:
                logger.error(f"Unsupported file format: {filepath.suffix}")
                return False
            
            # Initialize components
            self.cleaner = DataCleaner(self.data)
            self.analyzer = DataAnalyzer(self.data)
            self.visualizer = DataVisualizer(self.data)
            
            logger.info(f"Data loaded successfully: {self.data.shape}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return False
    
    def show_data_info(self):
        """Show comprehensive data information."""
        if self.data is None:
            logger.error("No data loaded")
            return
        
        info = self.cleaner.get_info()
        
        print("\n" + "="*50)
        print("DATA INFORMATION")
        print("="*50)
        print(f"Shape: {info['shape']}")
        print(f"Memory Usage: {info['memory_usage']:,} bytes")
        print(f"Columns: {len(info['columns'])}")
        
        print("\nColumn Types:")
        for col, dtype in info['dtypes'].items():
            print(f"  {col}: {dtype}")
        
        print(f"\nMissing Values: {info['missing_values']['total_missing']}")
        if info['missing_values']['columns_with_missing']:
            print("Columns with missing values:")
            for col, count in info['missing_values']['columns_with_missing'].items():
                pct = info['missing_values']['missing_percentage_by_column'][col]
                print(f"  {col}: {count} ({pct:.1f}%)")
        
        print(f"\nDuplicates: {info['duplicates']}")
        print(f"Numeric Columns: {len(info['numeric_columns'])}")
        print(f"Categorical Columns: {len(info['categorical_columns'])}")
        print(f"Datetime Columns: {len(info['datetime_columns'])}")
        print("="*50)
    
    def clean_data(self, args) -> bool:
        """
        Perform data cleaning operations.
        
        Args:
            args: Parsed arguments
            
        Returns:
            True if successful, False otherwise
        """
        if self.cleaner is None:
            logger.error("No data loaded")
            return False
        
        try:
            # Handle missing values
            if args.missing:
                fill_value = args.fill_value
                if fill_value is not None:
                    # Try to convert fill_value to appropriate type
                    try:
                        fill_value = float(fill_value)
                    except ValueError:
                        pass
                
                self.cleaner.handle_missing_values(
                    method=args.missing,
                    fill_value=fill_value
                )
            
            # Remove duplicates
            if args.remove_duplicates:
                self.cleaner.remove_duplicates()
            
            # Handle outliers
            if args.outliers:
                self.cleaner.handle_outliers(
                    method=args.outlier_method,
                    action=args.outliers,
                    threshold=args.outlier_threshold
                )
            
            # Convert data types
            if args.convert_types:
                self.cleaner.convert_data_types(auto_convert=True)
            
            # Validate data
            if args.validate:
                validation_results = self.cleaner.validate_data()
                if not validation_results['passed']:
                    logger.warning(f"Validation failed: {validation_results['errors']}")
                else:
                    logger.info("Data validation passed")
            
            # Update data in other components
            self.data = self.cleaner.data
            self.analyzer.load_data(self.data)
            self.visualizer.load_data(self.data)
            
            # Show cleaning summary
            summary = self.cleaner.get_cleaning_summary()
            print("\n" + "="*50)
            print("CLEANING SUMMARY")
            print("="*50)
            print(f"Original shape: {summary['original_shape']}")
            print(f"Current shape: {summary['current_shape']}")
            print("Operations performed:")
            for op in summary['cleaning_operations']:
                print(f"  - {op}")
            print("="*50)
            
            return True
            
        except Exception as e:
            logger.error(f"Error during cleaning: {e}")
            return False
    
    def perform_statistics(self, args) -> bool:
        """
        Perform statistical analysis.
        
        Args:
            args: Parsed arguments
            
        Returns:
            True if successful, False otherwise
        """
        if self.analyzer is None:
            logger.error("No data loaded")
            return False
        
        try:
            results = {}
            
            # Descriptive statistics
            if args.descriptive:
                desc_stats = self.analyzer.get_descriptive_stats()
                results['descriptive'] = desc_stats
                
                print("\n" + "="*50)
                print("DESCRIPTIVE STATISTICS")
                print("="*50)
                for col, stats in desc_stats.items():
                    print(f"\n{col}:")
                    print(f"  Count: {stats['count']}")
                    print(f"  Mean: {stats['mean']:.4f}")
                    print(f"  Median: {stats['median']:.4f}")
                    print(f"  Std: {stats['std']:.4f}")
                    print(f"  Min: {stats['min']:.4f}")
                    print(f"  Max: {stats['max']:.4f}")
                print("="*50)
            
            # Correlation analysis
            if args.correlation:
                corr_results = self.analyzer.get_correlation_matrix()
                results['correlation'] = corr_results
                
                print("\n" + "="*50)
                print("CORRELATION ANALYSIS")
                print("="*50)
                if 'strong_correlations' in corr_results:
                    print("Strong correlations found:")
                    for corr in corr_results['strong_correlations']:
                        print(f"  {corr['var1']} - {corr['var2']}: {corr['correlation']:.4f}")
                print("="*50)
            
            # Hypothesis testing
            if args.hypothesis:
                # This would need more specific parameters
                logger.info("Hypothesis testing requires specific parameters")
            
            # Regression analysis
            if args.regression:
                # This would need target and feature columns
                logger.info("Regression analysis requires target and feature columns")
            
            # Export results
            if args.export_results:
                self.analyzer.export_results(args.export_results, format='json')
                logger.info(f"Results exported to {args.export_results}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error during statistical analysis: {e}")
            return False
    
    def create_visualizations(self, args) -> bool:
        """
        Create data visualizations.
        
        Args:
            args: Parsed arguments
            
        Returns:
            True if successful, False otherwise
        """
        if self.visualizer is None:
            logger.error("No data loaded")
            return False
        
        try:
            # Set style
            self.visualizer.set_style(args.style)
            
            # Create plots
            if args.distributions:
                numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
                if numeric_cols:
                    self.visualizer.plot_multiple_distributions(numeric_cols[:4])
                    logger.info("Distribution plots created")
            
            if args.correlation_heatmap:
                self.visualizer.plot_correlation_heatmap()
                logger.info("Correlation heatmap created")
            
            if args.scatter_matrix:
                numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
                if len(numeric_cols) >= 2:
                    self.visualizer.plot_scatter_matrix(numeric_cols[:6])
                    logger.info("Scatter matrix created")
            
            # Save plots
            if args.save_plots:
                save_dir = Path(args.save_plots)
                save_dir.mkdir(exist_ok=True)
                
                for i, fig in enumerate(self.visualizer.figures):
                    filepath = save_dir / f"plot_{i+1}.png"
                    self.visualizer.save_plot(fig, str(filepath))
                
                logger.info(f"Plots saved to {save_dir}")
            
            # Show plots
            self.visualizer.show_all_plots()
            
            return True
            
        except Exception as e:
            logger.error(f"Error creating visualizations: {e}")
            return False
    
    def interactive_mode(self, args):
        """
        Start interactive mode.
        
        Args:
            args: Parsed arguments
        """
        print("\n" + "="*50)
        print("DataX Interactive Mode")
        print("="*50)
        print("Available commands:")
        print("  load <file>     - Load data from file")
        print("  info            - Show data information")
        print("  clean           - Start data cleaning")
        print("  stats           - Perform statistical analysis")
        print("  viz             - Create visualizations")
        print("  help            - Show this help")
        print("  quit/exit       - Exit interactive mode")
        print("="*50)
        
        # Load initial file if provided
        if args.file:
            if self.load_data(args.file):
                print(f"Data loaded: {self.data.shape}")
            else:
                print("Failed to load data")
        
        while True:
            try:
                command = input("\nDataX> ").strip().split()
                if not command:
                    continue
                
                cmd = command[0].lower()
                
                if cmd in ['quit', 'exit']:
                    print("Goodbye!")
                    break
                
                elif cmd == 'help':
                    print("Available commands: load, info, clean, stats, viz, help, quit")
                
                elif cmd == 'load':
                    if len(command) > 1:
                        if self.load_data(command[1]):
                            print(f"Data loaded: {self.data.shape}")
                        else:
                            print("Failed to load data")
                    else:
                        print("Usage: load <file>")
                
                elif cmd == 'info':
                    self.show_data_info()
                
                elif cmd == 'clean':
                    if self.data is not None:
                        print("Starting data cleaning...")
                        # Simple cleaning workflow
                        self.cleaner.handle_missing_values(method='auto')
                        self.cleaner.remove_duplicates()
                        self.data = self.cleaner.data
                        print("Basic cleaning completed")
                    else:
                        print("No data loaded")
                
                elif cmd == 'stats':
                    if self.data is not None:
                        print("Performing statistical analysis...")
                        desc_stats = self.analyzer.get_descriptive_stats()
                        print("Descriptive statistics calculated")
                    else:
                        print("No data loaded")
                
                elif cmd == 'viz':
                    if self.data is not None:
                        print("Creating visualizations...")
                        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
                        if numeric_cols:
                            self.visualizer.plot_multiple_distributions(numeric_cols[:4])
                            self.visualizer.show_all_plots()
                        print("Visualizations created")
                    else:
                        print("No data loaded")
                
                else:
                    print(f"Unknown command: {cmd}")
                    print("Type 'help' for available commands")
            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def run(self, args: Optional[List[str]] = None) -> int:
        """
        Run the CLI.
        
        Args:
            args: Command line arguments (None for sys.argv)
            
        Returns:
            Exit code
        """
        try:
            parsed_args = self.parser.parse_args(args)
            
            if parsed_args.verbose:
                logging.getLogger().setLevel(logging.DEBUG)
            
            if parsed_args.command is None:
                self.parser.print_help()
                return 1
            
            # Handle load command
            if parsed_args.command == 'load':
                if not self.load_data(parsed_args.file):
                    return 1
                
                if parsed_args.action == 'info':
                    self.show_data_info()
                elif parsed_args.action == 'clean':
                    self.clean_data(parsed_args)
                elif parsed_args.action == 'stats':
                    # Create a mock args object with default values for stats
                    import argparse
                    stats_args = argparse.Namespace(
                        descriptive=True,
                        correlation=True,
                        hypothesis=None,
                        regression=None,
                        anova=None,
                        normality=None,
                        export_results=None
                    )
                    self.perform_statistics(stats_args)
                elif parsed_args.action == 'viz':
                    # Create a mock args object with default values for viz
                    import argparse
                    viz_args = argparse.Namespace(
                        distributions=True,
                        correlation_heatmap=True,
                        scatter_matrix=False,
                        time_series=None,
                        categorical=None,
                        interactive=False,
                        style='default',
                        save_plots=None
                    )
                    self.create_visualizations(viz_args)
            
            # Handle other commands
            elif parsed_args.command == 'clean':
                if self.data is None:
                    logger.error("No data loaded. Use 'load' command first.")
                    return 1
                self.clean_data(parsed_args)
            
            elif parsed_args.command == 'stats':
                if self.data is None:
                    logger.error("No data loaded. Use 'load' command first.")
                    return 1
                self.perform_statistics(parsed_args)
            
            elif parsed_args.command == 'viz':
                if self.data is None:
                    logger.error("No data loaded. Use 'load' command first.")
                    return 1
                self.create_visualizations(parsed_args)
            
            elif parsed_args.command == 'interactive':
                self.interactive_mode(parsed_args)
            
            elif parsed_args.command == 'batch':
                logger.info("Batch processing not yet implemented")
                return 1
            
            return 0
            
        except Exception as e:
            logger.error(f"CLI error: {e}")
            return 1


def main():
    """Main entry point for CLI."""
    cli = DataXCLI()
    sys.exit(cli.run())


if __name__ == '__main__':
    main()
