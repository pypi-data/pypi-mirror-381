"""
Tests for the DataX visualization module.
"""

import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datax.viz import DataVisualizer
import tempfile
import os


class TestDataVisualizer:
    """Test cases for DataVisualizer class."""
    
    def test_init_with_data(self, sample_dataframe):
        """Test DataVisualizer initialization with data."""
        visualizer = DataVisualizer(sample_dataframe)
        assert visualizer.data is not None
        assert visualizer.style == 'default'
        assert len(visualizer.figures) == 0
    
    def test_init_without_data(self):
        """Test DataVisualizer initialization without data."""
        visualizer = DataVisualizer()
        assert visualizer.data is None
        assert visualizer.style == 'default'
    
    def test_init_with_style(self, sample_dataframe):
        """Test DataVisualizer initialization with custom style."""
        visualizer = DataVisualizer(sample_dataframe, style='dark')
        assert visualizer.style == 'dark'
    
    def test_load_data(self, sample_dataframe):
        """Test loading data into visualizer."""
        visualizer = DataVisualizer()
        result = visualizer.load_data(sample_dataframe)
        
        assert result is visualizer  # Method chaining
        assert visualizer.data is not None
        assert len(visualizer.figures) == 0
    
    def test_set_style(self, sample_dataframe):
        """Test setting visualization style."""
        visualizer = DataVisualizer(sample_dataframe)
        result = visualizer.set_style('dark')
        
        assert result is visualizer  # Method chaining
        assert visualizer.style == 'dark'
    
    def test_plot_distribution_histogram(self, sample_dataframe):
        """Test plotting histogram distribution."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_distribution('numeric_col', plot_type='histogram')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_distribution_density(self, sample_dataframe):
        """Test plotting density distribution."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_distribution('numeric_col', plot_type='density')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_distribution_box(self, sample_dataframe):
        """Test plotting box plot distribution."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_distribution('numeric_col', plot_type='box')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_distribution_violin(self, sample_dataframe):
        """Test plotting violin plot distribution."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_distribution('numeric_col', plot_type='violin')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_correlation_heatmap(self, correlation_data):
        """Test plotting correlation heatmap."""
        visualizer = DataVisualizer(correlation_data)
        fig = visualizer.plot_correlation_heatmap()
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_correlation_heatmap_specific_columns(self, correlation_data):
        """Test plotting correlation heatmap for specific columns."""
        visualizer = DataVisualizer(correlation_data)
        columns = ['var1', 'var2', 'var3']
        fig = visualizer.plot_correlation_heatmap(columns=columns)
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_correlation_heatmap_different_methods(self, correlation_data):
        """Test plotting correlation heatmap with different methods."""
        visualizer = DataVisualizer(correlation_data)
        
        # Test different correlation methods
        for method in ['pearson', 'spearman', 'kendall']:
            fig = visualizer.plot_correlation_heatmap(method=method)
            assert isinstance(fig, plt.Figure)
            plt.close(fig)
    
    def test_plot_scatter_matrix(self, correlation_data):
        """Test plotting scatter matrix."""
        visualizer = DataVisualizer(correlation_data)
        fig = visualizer.plot_scatter_matrix()
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_scatter_matrix_specific_columns(self, correlation_data):
        """Test plotting scatter matrix for specific columns."""
        visualizer = DataVisualizer(correlation_data)
        columns = ['var1', 'var2', 'var3']
        fig = visualizer.plot_scatter_matrix(columns=columns)
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_time_series_line(self, time_series_data):
        """Test plotting time series line plot."""
        visualizer = DataVisualizer(time_series_data)
        fig = visualizer.plot_time_series('date', 'value', style='line')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_time_series_scatter(self, time_series_data):
        """Test plotting time series scatter plot."""
        visualizer = DataVisualizer(time_series_data)
        fig = visualizer.plot_time_series('date', 'value', style='scatter')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_time_series_area(self, time_series_data):
        """Test plotting time series area plot."""
        visualizer = DataVisualizer(time_series_data)
        fig = visualizer.plot_time_series('date', 'value', style='area')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_categorical_analysis_count(self, sample_dataframe):
        """Test plotting categorical count analysis."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_categorical_analysis('categorical_col', plot_type='count')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_categorical_analysis_bar(self, sample_dataframe):
        """Test plotting categorical bar analysis."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_categorical_analysis('categorical_col', 
                                                 'numeric_col', 
                                                 plot_type='bar')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_categorical_analysis_box(self, sample_dataframe):
        """Test plotting categorical box plot analysis."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_categorical_analysis('categorical_col', 
                                                 'numeric_col', 
                                                 plot_type='box')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_categorical_analysis_violin(self, sample_dataframe):
        """Test plotting categorical violin plot analysis."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_categorical_analysis('categorical_col', 
                                                 'numeric_col', 
                                                 plot_type='violin')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_multiple_distributions_histogram(self, sample_dataframe):
        """Test plotting multiple distributions as histograms."""
        visualizer = DataVisualizer(sample_dataframe)
        columns = ['numeric_col', 'missing_col']
        fig = visualizer.plot_multiple_distributions(columns, plot_type='histogram')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_multiple_distributions_density(self, sample_dataframe):
        """Test plotting multiple distributions as density plots."""
        visualizer = DataVisualizer(sample_dataframe)
        columns = ['numeric_col', 'missing_col']
        fig = visualizer.plot_multiple_distributions(columns, plot_type='density')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_multiple_distributions_box(self, sample_dataframe):
        """Test plotting multiple distributions as box plots."""
        visualizer = DataVisualizer(sample_dataframe)
        columns = ['numeric_col', 'missing_col']
        fig = visualizer.plot_multiple_distributions(columns, plot_type='box')
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_statistical_summary(self, sample_dataframe):
        """Test plotting statistical summary."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_statistical_summary()
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_plot_statistical_summary_specific_columns(self, sample_dataframe):
        """Test plotting statistical summary for specific columns."""
        visualizer = DataVisualizer(sample_dataframe)
        columns = ['numeric_col', 'missing_col']
        fig = visualizer.plot_statistical_summary(columns=columns)
        
        assert isinstance(fig, plt.Figure)
        assert len(visualizer.figures) == 1
        plt.close(fig)
    
    def test_create_interactive_plot_scatter(self, correlation_data):
        """Test creating interactive scatter plot."""
        visualizer = DataVisualizer(correlation_data)
        fig = visualizer.create_interactive_plot('scatter', 
                                               x_column='var1', 
                                               y_column='var2')
        
        assert isinstance(fig, go.Figure)
    
    def test_create_interactive_plot_histogram(self, sample_dataframe):
        """Test creating interactive histogram."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.create_interactive_plot('histogram', column='numeric_col')
        
        assert isinstance(fig, go.Figure)
    
    def test_create_interactive_plot_heatmap(self, correlation_data):
        """Test creating interactive heatmap."""
        visualizer = DataVisualizer(correlation_data)
        fig = visualizer.create_interactive_plot('heatmap')
        
        assert isinstance(fig, go.Figure)
    
    def test_create_interactive_plot_box(self, sample_dataframe):
        """Test creating interactive box plot."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.create_interactive_plot('box', 
                                               value_column='numeric_col', 
                                               category_column='categorical_col')
        
        assert isinstance(fig, go.Figure)
    
    def test_save_plot_matplotlib(self, sample_dataframe, temp_file):
        """Test saving matplotlib plot."""
        visualizer = DataVisualizer(sample_dataframe)
        fig = visualizer.plot_distribution('numeric_col')
        
        output_path = temp_file.replace('.csv', '_plot.png')
        result = visualizer.save_plot(fig, output_path, format='png')
        
        assert result is visualizer  # Method chaining
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
        plt.close(fig)
    
    def test_save_plot_plotly(self, correlation_data, temp_file):
        """Test saving plotly plot."""
        visualizer = DataVisualizer(correlation_data)
        fig = visualizer.create_interactive_plot('scatter', 
                                               x_column='var1', 
                                               y_column='var2')
        
        output_path = temp_file.replace('.csv', '_plot.html')
        result = visualizer.save_plot(fig, output_path, format='html')
        
        assert result is visualizer
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
    
    def test_get_plot_summary(self, sample_dataframe):
        """Test getting plot summary."""
        visualizer = DataVisualizer(sample_dataframe)
        
        # Create some plots
        visualizer.plot_distribution('numeric_col')
        visualizer.plot_correlation_heatmap()
        
        summary = visualizer.get_plot_summary()
        
        assert 'total_plots' in summary
        assert 'plot_types' in summary
        assert 'style' in summary
        assert 'data_shape' in summary
        assert summary['total_plots'] == 2
    
    def test_error_handling_no_data(self):
        """Test error handling when no data is loaded."""
        visualizer = DataVisualizer()
        
        with pytest.raises(ValueError):
            visualizer.plot_distribution('column')
        
        with pytest.raises(ValueError):
            visualizer.plot_correlation_heatmap()
        
        with pytest.raises(ValueError):
            visualizer.create_interactive_plot('scatter', x_column='x', y_column='y')
    
    def test_error_handling_invalid_plot_type(self, sample_dataframe):
        """Test error handling with invalid plot type."""
        visualizer = DataVisualizer(sample_dataframe)
        
        with pytest.raises(ValueError):
            visualizer.plot_distribution('numeric_col', plot_type='invalid')
    
    def test_error_handling_invalid_interactive_plot_type(self, sample_dataframe):
        """Test error handling with invalid interactive plot type."""
        visualizer = DataVisualizer(sample_dataframe)
        
        with pytest.raises(ValueError):
            visualizer.create_interactive_plot('invalid_plot')
    
    def test_error_handling_insufficient_columns_correlation(self, mock_data):
        """Test error handling with insufficient columns for correlation."""
        visualizer = DataVisualizer(mock_data['single_col_df'])
        
        with pytest.raises(ValueError):
            visualizer.plot_correlation_heatmap()
    
    def test_error_handling_insufficient_columns_scatter_matrix(self, mock_data):
        """Test error handling with insufficient columns for scatter matrix."""
        visualizer = DataVisualizer(mock_data['single_col_df'])
        
        with pytest.raises(ValueError):
            visualizer.plot_scatter_matrix()
    
    def test_series_handling(self, sample_series):
        """Test handling of pandas Series."""
        visualizer = DataVisualizer(sample_series)
        
        # Should work with Series
        fig = visualizer.plot_distribution('test_series')
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_empty_dataframe(self, mock_data):
        """Test handling of empty DataFrame."""
        visualizer = DataVisualizer(mock_data['empty_df'])
        
        # Should handle empty DataFrame gracefully
        summary = visualizer.get_plot_summary()
        assert summary['data_shape'] == (0, 0)
    
    def test_single_column_dataframe(self, mock_data):
        """Test handling of single column DataFrame."""
        visualizer = DataVisualizer(mock_data['single_col_df'])
        
        # Should work with single column
        fig = visualizer.plot_distribution('col1')
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_mixed_types_dataframe(self, mock_data):
        """Test handling of DataFrame with mixed data types."""
        visualizer = DataVisualizer(mock_data['mixed_types_df'])
        
        # Should work with mixed types
        fig = visualizer.plot_distribution('int_col')
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_comprehensive_visualization_pipeline(self, correlation_data):
        """Test a comprehensive visualization pipeline."""
        visualizer = DataVisualizer(correlation_data, style='colorful')
        
        # Create multiple plots
        fig1 = visualizer.plot_distribution('var1', plot_type='histogram', kde=True)
        fig2 = visualizer.plot_correlation_heatmap(annot=True)
        fig3 = visualizer.plot_scatter_matrix()
        fig4 = visualizer.plot_multiple_distributions(['var1', 'var2', 'var3'])
        fig5 = visualizer.create_interactive_plot('scatter', x_column='var1', y_column='var2')
        
        # Check that all plots were created
        assert len(visualizer.figures) == 4  # Only matplotlib figures are stored
        assert isinstance(fig5, go.Figure)  # Plotly figure is returned separately
        
        # Get summary
        summary = visualizer.get_plot_summary()
        assert summary['total_plots'] == 4
        assert summary['style'] == 'colorful'
        
        # Cleanup
        for fig in [fig1, fig2, fig3, fig4]:
            plt.close(fig)
    
    def test_style_switching(self, sample_dataframe):
        """Test switching between different styles."""
        visualizer = DataVisualizer(sample_dataframe, style='default')
        
        # Test different styles
        for style in ['default', 'dark', 'minimal', 'colorful']:
            visualizer.set_style(style)
            assert visualizer.style == style
            
            # Create a plot to test style application
            fig = visualizer.plot_distribution('numeric_col')
            assert isinstance(fig, plt.Figure)
            plt.close(fig)
    
    def test_figure_management(self, sample_dataframe):
        """Test figure management and cleanup."""
        visualizer = DataVisualizer(sample_dataframe)
        
        # Create multiple figures
        fig1 = visualizer.plot_distribution('numeric_col')
        fig2 = visualizer.plot_correlation_heatmap()
        fig3 = visualizer.plot_statistical_summary()
        
        # Check that figures are stored
        assert len(visualizer.figures) == 3
        
        # Test show_all_plots (should not crash)
        visualizer.show_all_plots()
        
        # Cleanup
        for fig in [fig1, fig2, fig3]:
            plt.close(fig)
    
    def test_custom_figure_sizes(self, sample_dataframe):
        """Test creating plots with custom figure sizes."""
        visualizer = DataVisualizer(sample_dataframe)
        
        # Test different figure sizes
        fig1 = visualizer.plot_distribution('numeric_col', figsize=(8, 6))
        fig2 = visualizer.plot_correlation_heatmap(figsize=(12, 10))
        fig3 = visualizer.plot_multiple_distributions(['numeric_col', 'missing_col'], 
                                                     figsize=(15, 8))
        
        # Check that figures were created
        assert len(visualizer.figures) == 3
        
        # Cleanup
        for fig in [fig1, fig2, fig3]:
            plt.close(fig)
