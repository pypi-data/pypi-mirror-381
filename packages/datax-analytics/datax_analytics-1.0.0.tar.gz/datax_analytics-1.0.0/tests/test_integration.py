"""
Integration tests for the DataX package.
"""

import pytest
import pandas as pd
import numpy as np
import tempfile
import os
from datax import DataCleaner, DataAnalyzer, DataVisualizer
from datax.cli import DataXCLI


class TestIntegration:
    """Integration tests for DataX package."""
    
    def test_complete_data_analysis_pipeline(self, messy_dataframe):
        """Test complete data analysis pipeline."""
        # Step 1: Data Cleaning
        cleaner = DataCleaner(messy_dataframe)
        cleaner.handle_missing_values(method='auto') \
               .remove_duplicates() \
               .handle_outliers(method='iqr', action='cap') \
               .convert_data_types(auto_convert=True) \
               .validate_data()
        
        cleaned_data = cleaner.data
        
        # Step 2: Statistical Analysis
        analyzer = DataAnalyzer(cleaned_data)
        desc_stats = analyzer.get_descriptive_stats()
        corr_matrix = analyzer.get_correlation_matrix()
        
        # Step 3: Visualization
        visualizer = DataVisualizer(cleaned_data)
        visualizer.plot_distribution('age', plot_type='histogram', kde=True)
        visualizer.plot_correlation_heatmap()
        visualizer.plot_multiple_distributions(['age', 'salary', 'score'])
        
        # Verify results
        assert cleaned_data.shape[0] <= messy_dataframe.shape[0]
        assert len(desc_stats) > 0
        assert 'correlation_matrix' in corr_matrix
        assert len(visualizer.figures) == 3
        
        # Cleanup
        for fig in visualizer.figures:
            import matplotlib.pyplot as plt
            plt.close(fig)
    
    def test_cli_integration(self, temp_file):
        """Test CLI integration with real data."""
        cli = DataXCLI()
        
        # Test load and info
        result = cli.run(['load', temp_file, 'info'])
        assert result == 0
        assert cli.data is not None
        
        # Test cleaning
        result = cli.run(['clean', '--missing', 'auto', '--remove-duplicates'])
        assert result == 0
        
        # Test statistics
        result = cli.run(['stats', '--descriptive', '--correlation'])
        assert result == 0
        
        # Test visualization
        result = cli.run(['viz', '--distributions', '--correlation-heatmap'])
        assert result == 0
    
    def test_data_export_import_cycle(self, sample_dataframe, temp_dir):
        """Test data export and import cycle."""
        # Clean data
        cleaner = DataCleaner(sample_dataframe)
        cleaner.handle_missing_values(method='auto')
        
        # Export to different formats
        csv_path = os.path.join(temp_dir, 'data.csv')
        excel_path = os.path.join(temp_dir, 'data.xlsx')
        json_path = os.path.join(temp_dir, 'data.json')
        parquet_path = os.path.join(temp_dir, 'data.parquet')
        
        cleaner.save_cleaned_data(csv_path, format='csv')
        cleaner.save_cleaned_data(excel_path, format='excel')
        cleaner.save_cleaned_data(json_path, format='json')
        cleaner.save_cleaned_data(parquet_path, format='parquet')
        
        # Import and verify
        csv_data = pd.read_csv(csv_path)
        excel_data = pd.read_excel(excel_path)
        json_data = pd.read_json(json_path)
        parquet_data = pd.read_parquet(parquet_path)
        
        # All should have same shape
        assert csv_data.shape == excel_data.shape
        assert csv_data.shape == json_data.shape
        assert csv_data.shape == parquet_data.shape
    
    def test_statistical_analysis_workflow(self, correlation_data):
        """Test complete statistical analysis workflow."""
        analyzer = DataAnalyzer(correlation_data)
        
        # Descriptive statistics
        desc_stats = analyzer.get_descriptive_stats()
        
        # Correlation analysis
        corr_matrix = analyzer.get_correlation_matrix()
        
        # Hypothesis testing
        ttest_result = analyzer.hypothesis_test('ttest', 
                                              column1='var1', 
                                              column2='var2')
        
        # Regression analysis
        regression = analyzer.regression_analysis('var1', ['var2', 'var3'])
        
        # ANOVA analysis
        anova = analyzer.anova_analysis('var1', 'category')
        
        # Normality testing
        normality = analyzer.hypothesis_test('normality', 
                                           column='var1', 
                                           test='shapiro')
        
        # Export results
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
            analyzer.export_results(f.name, format='json')
            assert os.path.exists(f.name)
            os.unlink(f.name)
        
        # Verify all analyses were performed
        assert len(desc_stats) > 0
        assert 'correlation_matrix' in corr_matrix
        assert ttest_result['test_type'] == 'two_sample'
        assert regression['method'] == 'linear_regression'
        assert anova['test_type'] == 'one_way_anova'
        assert normality['test_type'] == 'normality_shapiro'
    
    def test_visualization_workflow(self, time_series_data):
        """Test complete visualization workflow."""
        visualizer = DataVisualizer(time_series_data, style='colorful')
        
        # Distribution plots
        fig1 = visualizer.plot_distribution('value', plot_type='histogram', kde=True)
        fig2 = visualizer.plot_distribution('value', plot_type='density')
        fig3 = visualizer.plot_distribution('value', plot_type='box')
        fig4 = visualizer.plot_distribution('value', plot_type='violin')
        
        # Time series plots
        fig5 = visualizer.plot_time_series('date', 'value', style='line')
        fig6 = visualizer.plot_time_series('date', 'value', style='scatter')
        fig7 = visualizer.plot_time_series('date', 'value', style='area')
        
        # Categorical analysis
        fig8 = visualizer.plot_categorical_analysis('category', plot_type='count')
        fig9 = visualizer.plot_categorical_analysis('category', 'value', plot_type='bar')
        fig10 = visualizer.plot_categorical_analysis('category', 'value', plot_type='box')
        fig11 = visualizer.plot_categorical_analysis('category', 'value', plot_type='violin')
        
        # Multiple distributions
        fig12 = visualizer.plot_multiple_distributions(['value'])
        
        # Statistical summary
        fig13 = visualizer.plot_statistical_summary()
        
        # Interactive plots
        interactive_fig1 = visualizer.create_interactive_plot('scatter', 
                                                            x_column='date', 
                                                            y_column='value')
        interactive_fig2 = visualizer.create_interactive_plot('histogram', 
                                                            column='value')
        interactive_fig3 = visualizer.create_interactive_plot('box', 
                                                            value_column='value', 
                                                            category_column='category')
        
        # Save plots
        with tempfile.TemporaryDirectory() as temp_dir:
            for i, fig in enumerate(visualizer.figures):
                visualizer.save_plot(fig, os.path.join(temp_dir, f'plot_{i}.png'))
            
            # Save interactive plots
            visualizer.save_plot(interactive_fig1, os.path.join(temp_dir, 'interactive1.html'))
            visualizer.save_plot(interactive_fig2, os.path.join(temp_dir, 'interactive2.html'))
            visualizer.save_plot(interactive_fig3, os.path.join(temp_dir, 'interactive3.html'))
            
            # Verify files were created
            assert len(os.listdir(temp_dir)) >= 13
        
        # Get summary
        summary = visualizer.get_plot_summary()
        assert summary['total_plots'] == 13
        assert summary['style'] == 'colorful'
        
        # Cleanup
        import matplotlib.pyplot as plt
        for fig in visualizer.figures:
            plt.close(fig)
    
    def test_error_handling_integration(self, mock_data):
        """Test error handling across modules."""
        # Test with empty DataFrame
        cleaner = DataCleaner(mock_data['empty_df'])
        analyzer = DataAnalyzer(mock_data['empty_df'])
        visualizer = DataVisualizer(mock_data['empty_df'])
        
        # Should handle gracefully
        info = cleaner.get_info()
        assert info['shape'] == (0, 0)
        
        stats = analyzer.get_descriptive_stats()
        assert 'error' in stats
        
        summary = visualizer.get_plot_summary()
        assert summary['data_shape'] == (0, 0)
        
        # Test with single column DataFrame
        cleaner = DataCleaner(mock_data['single_col_df'])
        analyzer = DataAnalyzer(mock_data['single_col_df'])
        visualizer = DataVisualizer(mock_data['single_col_df'])
        
        # Should work with single column
        info = cleaner.get_info()
        assert info['shape'][1] == 1
        
        stats = analyzer.get_descriptive_stats()
        assert len(stats) > 0
        
        fig = visualizer.plot_distribution('col1')
        assert fig is not None
        import matplotlib.pyplot as plt
        plt.close(fig)
        
        # Test with all NaN DataFrame
        cleaner = DataCleaner(mock_data['all_nan_df'])
        analyzer = DataAnalyzer(mock_data['all_nan_df'])
        
        # Should handle gracefully
        info = cleaner.get_info()
        assert info['shape'] == (2, 2)
        
        stats = analyzer.get_descriptive_stats()
        assert isinstance(stats, dict)
    
    def test_performance_with_large_dataset(self):
        """Test performance with larger dataset."""
        # Create larger dataset
        np.random.seed(42)
        large_data = pd.DataFrame({
            'col1': np.random.normal(0, 1, 10000),
            'col2': np.random.normal(0, 1, 10000),
            'col3': np.random.normal(0, 1, 10000),
            'category': np.random.choice(['A', 'B', 'C'], 10000)
        })
        
        # Add some missing values
        large_data.loc[1000:1100, 'col1'] = np.nan
        large_data.loc[2000:2100, 'col2'] = np.nan
        
        # Test cleaning performance
        cleaner = DataCleaner(large_data)
        cleaner.handle_missing_values(method='auto')
        cleaner.remove_duplicates()
        cleaner.handle_outliers(method='iqr', action='cap')
        
        # Test analysis performance
        analyzer = DataAnalyzer(cleaner.data)
        desc_stats = analyzer.get_descriptive_stats()
        corr_matrix = analyzer.get_correlation_matrix()
        
        # Test visualization performance
        visualizer = DataVisualizer(analyzer.data)
        visualizer.plot_distribution('col1')
        visualizer.plot_correlation_heatmap()
        visualizer.plot_multiple_distributions(['col1', 'col2', 'col3'])
        
        # Verify results
        assert len(desc_stats) == 3
        assert 'correlation_matrix' in corr_matrix
        assert len(visualizer.figures) == 3
        
        # Cleanup
        import matplotlib.pyplot as plt
        for fig in visualizer.figures:
            plt.close(fig)
    
    def test_memory_efficiency(self, sample_dataframe):
        """Test memory efficiency of operations."""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Perform multiple operations
        for i in range(10):
            cleaner = DataCleaner(sample_dataframe)
            cleaner.handle_missing_values(method='auto')
            cleaner.remove_duplicates()
            
            analyzer = DataAnalyzer(cleaner.data)
            analyzer.get_descriptive_stats()
            analyzer.get_correlation_matrix()
            
            visualizer = DataVisualizer(analyzer.data)
            visualizer.plot_distribution('numeric_col')
            
            # Cleanup
            import matplotlib.pyplot as plt
            for fig in visualizer.figures:
                plt.close(fig)
        
        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory
        
        # Memory increase should be reasonable (less than 100MB)
        assert memory_increase < 100 * 1024 * 1024
    
    def test_concurrent_operations(self, sample_dataframe):
        """Test concurrent operations on same data."""
        import threading
        import time
        
        results = []
        
        def clean_data():
            cleaner = DataCleaner(sample_dataframe)
            cleaner.handle_missing_values(method='auto')
            results.append(('clean', cleaner.data.shape))
        
        def analyze_data():
            analyzer = DataAnalyzer(sample_dataframe)
            stats = analyzer.get_descriptive_stats()
            results.append(('analyze', len(stats)))
        
        def visualize_data():
            visualizer = DataVisualizer(sample_dataframe)
            visualizer.plot_distribution('numeric_col')
            results.append(('visualize', len(visualizer.figures)))
        
        # Run operations concurrently
        threads = []
        for func in [clean_data, analyze_data, visualize_data]:
            thread = threading.Thread(target=func)
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Verify all operations completed
        assert len(results) == 3
        assert any(result[0] == 'clean' for result in results)
        assert any(result[0] == 'analyze' for result in results)
        assert any(result[0] == 'visualize' for result in results)
    
    def test_data_consistency_across_modules(self, sample_dataframe):
        """Test data consistency across different modules."""
        # Clean data
        cleaner = DataCleaner(sample_dataframe)
        cleaner.handle_missing_values(method='auto')
        cleaned_data = cleaner.data
        
        # Pass to analyzer
        analyzer = DataAnalyzer(cleaned_data)
        desc_stats = analyzer.get_descriptive_stats()
        
        # Pass to visualizer
        visualizer = DataVisualizer(cleaned_data)
        visualizer.plot_distribution('numeric_col')
        
        # Verify data consistency
        assert analyzer.data.shape == cleaned_data.shape
        assert visualizer.data.shape == cleaned_data.shape
        assert analyzer.data.equals(cleaned_data)
        assert visualizer.data.equals(cleaned_data)
        
        # Verify statistics match data
        for col in desc_stats:
            if col in cleaned_data.columns:
                assert desc_stats[col]['count'] == len(cleaned_data[col].dropna())
        
        # Cleanup
        import matplotlib.pyplot as plt
        for fig in visualizer.figures:
            plt.close(fig)
    
    def test_comprehensive_validation(self, messy_dataframe):
        """Test comprehensive data validation."""
        # Define validation rules
        validation_rules = {
            "age_range": {
                "type": "range",
                "column": "age",
                "min": 18,
                "max": 80
            },
            "salary_positive": {
                "type": "range",
                "column": "salary",
                "min": 0
            },
            "unique_id": {
                "type": "unique",
                "column": "id"
            }
        }
        
        # Clean data
        cleaner = DataCleaner(messy_dataframe)
        cleaner.handle_missing_values(method='auto') \
               .remove_duplicates() \
               .handle_outliers(method='iqr', action='cap')
        
        # Validate data
        validation_results = cleaner.validate_data(rules=validation_rules)
        
        # If validation fails, fix issues
        if not validation_results['passed']:
            # Fix age issues
            cleaner.data.loc[cleaner.data['age'] > 80, 'age'] = 80
            cleaner.data.loc[cleaner.data['age'] < 18, 'age'] = 18
            
            # Fix salary issues
            cleaner.data.loc[cleaner.data['salary'] < 0, 'salary'] = 0
            
            # Re-validate
            validation_results = cleaner.validate_data(rules=validation_rules)
        
        # Should pass validation now
        assert validation_results['passed']
        
        # Continue with analysis
        analyzer = DataAnalyzer(cleaner.data)
        desc_stats = analyzer.get_descriptive_stats()
        
        # Verify statistics are reasonable
        age_stats = desc_stats.get('age', {})
        if age_stats:
            assert 18 <= age_stats['min'] <= age_stats['max'] <= 80
        
        salary_stats = desc_stats.get('salary', {})
        if salary_stats:
            assert salary_stats['min'] >= 0
