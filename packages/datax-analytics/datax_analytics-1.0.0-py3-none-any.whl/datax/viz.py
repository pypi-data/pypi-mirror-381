"""
Data Visualization Module for DataX Package

This module provides comprehensive data visualization functionality including:
- Statistical plots
- Distribution plots
- Correlation plots
- Time series plots
- Advanced interactive visualizations
- Customizable styling and themes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union, List, Dict, Any, Optional, Tuple
import warnings
from matplotlib.patches import Rectangle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.offline as pyo
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set default style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


class DataVisualizer:
    """
    Advanced data visualization class with comprehensive plotting methods.
    
    This class provides a wide range of visualization options including
    statistical plots, distribution plots, correlation plots, time series
    plots, and interactive visualizations.
    """
    
    def __init__(self, data: Union[pd.DataFrame, pd.Series] = None, style: str = 'default'):
        """
        Initialize DataVisualizer with optional data.
        
        Args:
            data: pandas DataFrame or Series to visualize
            style: Plotting style ('default', 'dark', 'minimal', 'colorful')
        """
        self.data = data.copy() if data is not None else None
        self.style = style
        self.figures = []
        self._setup_style()
        
    def _setup_style(self):
        """Setup plotting style."""
        if self.style == 'dark':
            plt.style.use('dark_background')
            sns.set_style("darkgrid")
        elif self.style == 'minimal':
            plt.style.use('default')
            sns.set_style("whitegrid")
        elif self.style == 'colorful':
            plt.style.use('seaborn-v0_8')
            sns.set_palette("Set2")
        else:
            plt.style.use('seaborn-v0_8')
            sns.set_palette("husl")
    
    def load_data(self, data: Union[pd.DataFrame, pd.Series]) -> 'DataVisualizer':
        """
        Load data into the visualizer.
        
        Args:
            data: pandas DataFrame or Series
            
        Returns:
            self for method chaining
        """
        self.data = data.copy()
        self.figures = []
        logger.info(f"Data loaded for visualization: {data.shape}")
        return self
    
    def set_style(self, style: str) -> 'DataVisualizer':
        """
        Set plotting style.
        
        Args:
            style: Plotting style
            
        Returns:
            self for method chaining
        """
        self.style = style
        self._setup_style()
        return self
    
    def plot_distribution(self, 
                         column: str,
                         plot_type: str = 'histogram',
                         bins: int = 30,
                         kde: bool = True,
                         figsize: Tuple[int, int] = (10, 6)) -> plt.Figure:
        """
        Plot distribution of a single column.
        
        Args:
            column: Column to plot
            plot_type: Type of plot ('histogram', 'density', 'box', 'violin')
            bins: Number of bins for histogram
            kde: Whether to show KDE curve
            figsize: Figure size
            
        Returns:
            matplotlib Figure object
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        fig, ax = plt.subplots(figsize=figsize)
        data_series = self.data[column].dropna()
        
        if plot_type == 'histogram':
            ax.hist(data_series, bins=bins, alpha=0.7, edgecolor='black')
            if kde:
                from scipy.stats import gaussian_kde
                kde_curve = gaussian_kde(data_series)
                x_range = np.linspace(data_series.min(), data_series.max(), 100)
                ax.plot(x_range, kde_curve(x_range) * len(data_series) * (data_series.max() - data_series.min()) / bins, 
                       'r-', linewidth=2, label='KDE')
                ax.legend()
        
        elif plot_type == 'density':
            data_series.plot.kde(ax=ax)
        
        elif plot_type == 'box':
            ax.boxplot(data_series, vert=True)
            ax.set_ylabel(column)
        
        elif plot_type == 'violin':
            ax.violinplot([data_series], positions=[1], showmeans=True, showmedians=True)
            ax.set_ylabel(column)
            ax.set_xticks([1])
            ax.set_xticklabels([column])
        
        ax.set_title(f'Distribution of {column}')
        ax.grid(True, alpha=0.3)
        
        self.figures.append(fig)
        return fig
    
    def plot_correlation_heatmap(self, 
                                columns: Optional[List[str]] = None,
                                method: str = 'pearson',
                                figsize: Tuple[int, int] = (10, 8),
                                annot: bool = True) -> plt.Figure:
        """
        Plot correlation heatmap.
        
        Args:
            columns: Columns to include in correlation
            method: Correlation method
            figsize: Figure size
            annot: Whether to annotate with correlation values
            
        Returns:
            matplotlib Figure object
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if columns is None:
            columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(columns) < 2:
            raise ValueError("Need at least 2 numeric columns for correlation")
        
        fig, ax = plt.subplots(figsize=figsize)
        correlation_matrix = self.data[columns].corr(method=method)
        
        sns.heatmap(correlation_matrix, 
                   annot=annot, 
                   cmap='coolwarm', 
                   center=0,
                   square=True,
                   ax=ax,
                   fmt='.2f')
        
        ax.set_title(f'Correlation Heatmap ({method.title()})')
        
        self.figures.append(fig)
        return fig
    
    def plot_scatter_matrix(self, 
                           columns: Optional[List[str]] = None,
                           figsize: Tuple[int, int] = (12, 12),
                           diagonal: str = 'hist') -> plt.Figure:
        """
        Plot scatter matrix for multiple columns.
        
        Args:
            columns: Columns to include
            figsize: Figure size
            diagonal: What to show on diagonal ('hist', 'kde', 'scatter')
            
        Returns:
            matplotlib Figure object
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if columns is None:
            columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(columns) < 2:
            raise ValueError("Need at least 2 numeric columns for scatter matrix")
        
        fig = plt.figure(figsize=figsize)
        pd.plotting.scatter_matrix(self.data[columns], 
                                 diagonal=diagonal,
                                 alpha=0.6,
                                 figsize=figsize)
        
        plt.suptitle('Scatter Matrix', fontsize=16)
        
        self.figures.append(fig)
        return fig
    
    def plot_time_series(self, 
                        time_column: str,
                        value_column: str,
                        figsize: Tuple[int, int] = (12, 6),
                        style: str = 'line') -> plt.Figure:
        """
        Plot time series data.
        
        Args:
            time_column: Time/date column
            value_column: Value column to plot
            figsize: Figure size
            style: Plot style ('line', 'scatter', 'area')
            
        Returns:
            matplotlib Figure object
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        fig, ax = plt.subplots(figsize=figsize)
        
        # Convert time column to datetime if needed
        time_data = pd.to_datetime(self.data[time_column])
        value_data = self.data[value_column]
        
        if style == 'line':
            ax.plot(time_data, value_data, linewidth=2)
        elif style == 'scatter':
            ax.scatter(time_data, value_data, alpha=0.6)
        elif style == 'area':
            ax.fill_between(time_data, value_data, alpha=0.6)
        
        ax.set_xlabel(time_column)
        ax.set_ylabel(value_column)
        ax.set_title(f'Time Series: {value_column} over {time_column}')
        ax.grid(True, alpha=0.3)
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        self.figures.append(fig)
        return fig
    
    def plot_categorical_analysis(self, 
                                 category_column: str,
                                 value_column: Optional[str] = None,
                                 plot_type: str = 'count',
                                 figsize: Tuple[int, int] = (10, 6)) -> plt.Figure:
        """
        Plot categorical data analysis.
        
        Args:
            category_column: Categorical column
            value_column: Numeric column for aggregation (optional)
            plot_type: Type of plot ('count', 'bar', 'box', 'violin')
            figsize: Figure size
            
        Returns:
            matplotlib Figure object
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        fig, ax = plt.subplots(figsize=figsize)
        
        if plot_type == 'count':
            category_counts = self.data[category_column].value_counts()
            category_counts.plot(kind='bar', ax=ax)
            ax.set_title(f'Count of {category_column}')
            ax.set_ylabel('Count')
        
        elif plot_type == 'bar' and value_column:
            category_means = self.data.groupby(category_column)[value_column].mean()
            category_means.plot(kind='bar', ax=ax)
            ax.set_title(f'Mean {value_column} by {category_column}')
            ax.set_ylabel(f'Mean {value_column}')
        
        elif plot_type == 'box' and value_column:
            self.data.boxplot(column=value_column, by=category_column, ax=ax)
            ax.set_title(f'Distribution of {value_column} by {category_column}')
            ax.set_xlabel(category_column)
            ax.set_ylabel(value_column)
        
        elif plot_type == 'violin' and value_column:
            categories = self.data[category_column].unique()
            data_by_category = [self.data[self.data[category_column] == cat][value_column].dropna() 
                              for cat in categories]
            ax.violinplot(data_by_category, positions=range(len(categories)))
            ax.set_xticks(range(len(categories)))
            ax.set_xticklabels(categories)
            ax.set_title(f'Distribution of {value_column} by {category_column}')
            ax.set_xlabel(category_column)
            ax.set_ylabel(value_column)
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        self.figures.append(fig)
        return fig
    
    def plot_multiple_distributions(self, 
                                   columns: List[str],
                                   plot_type: str = 'histogram',
                                   figsize: Tuple[int, int] = (15, 10)) -> plt.Figure:
        """
        Plot distributions of multiple columns.
        
        Args:
            columns: List of columns to plot
            plot_type: Type of plot ('histogram', 'density', 'box')
            figsize: Figure size
            
        Returns:
            matplotlib Figure object
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        n_cols = len(columns)
        n_rows = (n_cols + 2) // 3  # 3 columns per row
        
        fig, axes = plt.subplots(n_rows, 3, figsize=figsize)
        axes = axes.flatten() if n_rows > 1 else [axes] if n_cols == 1 else axes
        
        for i, col in enumerate(columns):
            if i >= len(axes):
                break
                
            data_series = self.data[col].dropna()
            
            if plot_type == 'histogram':
                axes[i].hist(data_series, bins=30, alpha=0.7, edgecolor='black')
            elif plot_type == 'density':
                data_series.plot.kde(ax=axes[i])
            elif plot_type == 'box':
                axes[i].boxplot(data_series)
            
            axes[i].set_title(f'Distribution of {col}')
            axes[i].grid(True, alpha=0.3)
        
        # Hide unused subplots
        for i in range(len(columns), len(axes)):
            axes[i].set_visible(False)
        
        plt.tight_layout()
        
        self.figures.append(fig)
        return fig
    
    def create_interactive_plot(self, 
                               plot_type: str,
                               **kwargs) -> go.Figure:
        """
        Create interactive plot using Plotly.
        
        Args:
            plot_type: Type of interactive plot
            **kwargs: Plot-specific parameters
            
        Returns:
            Plotly Figure object
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if plot_type == 'scatter':
            return self._create_interactive_scatter(**kwargs)
        elif plot_type == 'histogram':
            return self._create_interactive_histogram(**kwargs)
        elif plot_type == 'heatmap':
            return self._create_interactive_heatmap(**kwargs)
        elif plot_type == 'box':
            return self._create_interactive_box(**kwargs)
        else:
            raise ValueError(f"Unsupported interactive plot type: {plot_type}")
    
    def _create_interactive_scatter(self, 
                                   x_column: str,
                                   y_column: str,
                                   color_column: Optional[str] = None,
                                   size_column: Optional[str] = None) -> go.Figure:
        """Create interactive scatter plot."""
        fig = px.scatter(self.data, 
                        x=x_column, 
                        y=y_column,
                        color=color_column,
                        size=size_column,
                        hover_data=self.data.columns.tolist())
        
        fig.update_layout(
            title=f'Interactive Scatter: {y_column} vs {x_column}',
            xaxis_title=x_column,
            yaxis_title=y_column
        )
        
        return fig
    
    def _create_interactive_histogram(self, 
                                     column: str,
                                     bins: int = 30) -> go.Figure:
        """Create interactive histogram."""
        fig = px.histogram(self.data, 
                          x=column,
                          nbins=bins,
                          title=f'Interactive Histogram: {column}')
        
        return fig
    
    def _create_interactive_heatmap(self, 
                                   columns: Optional[List[str]] = None) -> go.Figure:
        """Create interactive correlation heatmap."""
        if columns is None:
            columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
        
        correlation_matrix = self.data[columns].corr()
        
        fig = px.imshow(correlation_matrix,
                       text_auto=True,
                       aspect="auto",
                       title="Interactive Correlation Heatmap")
        
        return fig
    
    def _create_interactive_box(self, 
                               value_column: str,
                               category_column: str) -> go.Figure:
        """Create interactive box plot."""
        fig = px.box(self.data,
                    x=category_column,
                    y=value_column,
                    title=f'Interactive Box Plot: {value_column} by {category_column}')
        
        return fig
    
    def plot_statistical_summary(self, 
                                columns: Optional[List[str]] = None,
                                figsize: Tuple[int, int] = (15, 10)) -> plt.Figure:
        """
        Create comprehensive statistical summary plot.
        
        Args:
            columns: Columns to include in summary
            figsize: Figure size
            
        Returns:
            matplotlib Figure object
        """
        if self.data is None:
            raise ValueError("No data loaded")
        
        if columns is None:
            columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
        
        n_cols = len(columns)
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # 1. Distribution plots
        for i, col in enumerate(columns[:4]):  # Show up to 4 columns
            row, col_idx = i // 2, i % 2
            data_series = self.data[col].dropna()
            axes[row, col_idx].hist(data_series, bins=30, alpha=0.7, edgecolor='black')
            axes[row, col_idx].set_title(f'Distribution of {col}')
            axes[row, col_idx].grid(True, alpha=0.3)
        
        # Hide unused subplots
        for i in range(len(columns), 4):
            row, col_idx = i // 2, i % 2
            axes[row, col_idx].set_visible(False)
        
        plt.suptitle('Statistical Summary', fontsize=16)
        plt.tight_layout()
        
        self.figures.append(fig)
        return fig
    
    def save_plot(self, 
                  figure: Union[plt.Figure, go.Figure],
                  filepath: str,
                  format: str = 'png',
                  dpi: int = 300) -> 'DataVisualizer':
        """
        Save plot to file.
        
        Args:
            figure: Figure to save
            filepath: Path to save the file
            format: File format ('png', 'jpg', 'pdf', 'svg', 'html')
            dpi: DPI for raster formats
            
        Returns:
            self for method chaining
        """
        if isinstance(figure, plt.Figure):
            figure.savefig(filepath, format=format, dpi=dpi, bbox_inches='tight')
        elif isinstance(figure, go.Figure):
            if format == 'html':
                figure.write_html(filepath)
            else:
                figure.write_image(filepath, format=format, width=1200, height=800)
        
        logger.info(f"Plot saved to {filepath}")
        return self
    
    def show_all_plots(self):
        """Display all created plots."""
        for fig in self.figures:
            if isinstance(fig, plt.Figure):
                plt.show()
    
    def get_plot_summary(self) -> Dict[str, Any]:
        """
        Get summary of all created plots.
        
        Returns:
            Dictionary with plot summary
        """
        return {
            "total_plots": len(self.figures),
            "plot_types": [type(fig).__name__ for fig in self.figures],
            "style": self.style,
            "data_shape": self.data.shape if self.data is not None else None
        }
