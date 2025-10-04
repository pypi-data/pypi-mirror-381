"""
Tests for the DataX stats module.
"""

import pytest
import pandas as pd
import numpy as np
from datax.stats import DataAnalyzer
import tempfile
import os


class TestDataAnalyzer:
    """Test cases for DataAnalyzer class."""
    
    def test_init_with_data(self, sample_dataframe):
        """Test DataAnalyzer initialization with data."""
        analyzer = DataAnalyzer(sample_dataframe)
        assert analyzer.data is not None
        assert len(analyzer.analysis_results) == 0
    
    def test_init_without_data(self):
        """Test DataAnalyzer initialization without data."""
        analyzer = DataAnalyzer()
        assert analyzer.data is None
    
    def test_load_data(self, sample_dataframe):
        """Test loading data into analyzer."""
        analyzer = DataAnalyzer()
        result = analyzer.load_data(sample_dataframe)
        
        assert result is analyzer  # Method chaining
        assert analyzer.data is not None
        assert len(analyzer.analysis_results) == 0
    
    def test_get_descriptive_stats_basic(self, sample_dataframe):
        """Test basic descriptive statistics."""
        analyzer = DataAnalyzer(sample_dataframe)
        stats = analyzer.get_descriptive_stats()
        
        assert isinstance(stats, dict)
        assert len(stats) > 0
        
        # Check that numeric columns have statistics
        for col, col_stats in stats.items():
            assert 'count' in col_stats
            assert 'mean' in col_stats
            assert 'median' in col_stats
            assert 'std' in col_stats
            assert 'min' in col_stats
            assert 'max' in col_stats
    
    def test_get_descriptive_stats_include_all(self, sample_dataframe):
        """Test descriptive statistics with all measures."""
        analyzer = DataAnalyzer(sample_dataframe)
        stats = analyzer.get_descriptive_stats(include_all=True)
        
        # Check for additional statistics
        for col, col_stats in stats.items():
            assert 'sum' in col_stats
            assert 'sem' in col_stats
            assert 'mad' in col_stats
            assert 'cv' in col_stats
            assert 'percentiles' in col_stats
    
    def test_get_descriptive_stats_specific_columns(self, sample_dataframe):
        """Test descriptive statistics for specific columns."""
        analyzer = DataAnalyzer(sample_dataframe)
        columns = ['numeric_col', 'missing_col']
        stats = analyzer.get_descriptive_stats(columns=columns)
        
        assert len(stats) == len(columns)
        for col in columns:
            assert col in stats
    
    def test_get_correlation_matrix_pearson(self, correlation_data):
        """Test Pearson correlation matrix."""
        analyzer = DataAnalyzer(correlation_data)
        corr = analyzer.get_correlation_matrix(method='pearson')
        
        assert 'correlation_matrix' in corr
        assert 'strong_correlations' in corr
        assert 'method' in corr
        assert 'data_points' in corr
        assert corr['method'] == 'pearson'
    
    def test_get_correlation_matrix_spearman(self, correlation_data):
        """Test Spearman correlation matrix."""
        analyzer = DataAnalyzer(correlation_data)
        corr = analyzer.get_correlation_matrix(method='spearman')
        
        assert corr['method'] == 'spearman'
    
    def test_get_correlation_matrix_kendall(self, correlation_data):
        """Test Kendall correlation matrix."""
        analyzer = DataAnalyzer(correlation_data)
        corr = analyzer.get_correlation_matrix(method='kendall')
        
        assert corr['method'] == 'kendall'
    
    def test_get_correlation_matrix_specific_columns(self, correlation_data):
        """Test correlation matrix for specific columns."""
        analyzer = DataAnalyzer(correlation_data)
        columns = ['var1', 'var2', 'var3']
        corr = analyzer.get_correlation_matrix(columns=columns)
        
        assert 'correlation_matrix' in corr
        # Check that only specified columns are included
        corr_matrix = corr['correlation_matrix']
        assert all(col in corr_matrix for col in columns)
    
    def test_hypothesis_test_ttest_one_sample(self, sample_dataframe):
        """Test one-sample t-test."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.hypothesis_test('ttest', column1='numeric_col', mu=100)
        
        assert result['test_type'] == 'one_sample'
        assert 'statistic' in result
        assert 'p_value' in result
        assert 'significant' in result
        assert 'columns' in result
    
    def test_hypothesis_test_ttest_two_sample(self, sample_dataframe):
        """Test two-sample t-test."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.hypothesis_test('ttest', 
                                        column1='numeric_col', 
                                        column2='missing_col')
        
        assert result['test_type'] == 'two_sample'
        assert 'statistic' in result
        assert 'p_value' in result
        assert 'significant' in result
    
    def test_hypothesis_test_chi2(self, sample_dataframe):
        """Test chi-square test."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.hypothesis_test('chi2', 
                                        column1='categorical_col', 
                                        column2='duplicate_col')
        
        assert result['test_type'] == 'chi2_independence'
        assert 'chi2_statistic' in result
        assert 'p_value' in result
        assert 'degrees_of_freedom' in result
        assert 'contingency_table' in result
    
    def test_hypothesis_test_mannwhitney(self, sample_dataframe):
        """Test Mann-Whitney U test."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.hypothesis_test('mannwhitney', 
                                        column1='numeric_col', 
                                        column2='missing_col')
        
        assert result['test_type'] == 'mannwhitney'
        assert 'statistic' in result
        assert 'p_value' in result
        assert 'significant' in result
    
    def test_hypothesis_test_kruskal(self, sample_dataframe):
        """Test Kruskal-Wallis test."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.hypothesis_test('kruskal', 
                                        value_column='numeric_col', 
                                        group_column='categorical_col')
        
        assert result['test_type'] == 'kruskal_wallis'
        assert 'statistic' in result
        assert 'p_value' in result
        assert 'significant' in result
        assert 'groups' in result
    
    def test_hypothesis_test_normality_shapiro(self, sample_dataframe):
        """Test Shapiro-Wilk normality test."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.hypothesis_test('normality', 
                                        column='numeric_col', 
                                        test='shapiro')
        
        assert result['test_type'] == 'normality_shapiro'
        assert 'statistic' in result
        assert 'p_value' in result
        assert 'normal' in result
        assert 'column' in result
    
    def test_hypothesis_test_normality_kstest(self, sample_dataframe):
        """Test Kolmogorov-Smirnov normality test."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.hypothesis_test('normality', 
                                        column='numeric_col', 
                                        test='kstest')
        
        assert result['test_type'] == 'normality_kstest'
        assert 'statistic' in result
        assert 'p_value' in result
        assert 'normal' in result
    
    def test_hypothesis_test_normality_jarque_bera(self, sample_dataframe):
        """Test Jarque-Bera normality test."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.hypothesis_test('normality', 
                                        column='numeric_col', 
                                        test='jarque_bera')
        
        assert result['test_type'] == 'normality_jarque_bera'
        assert 'statistic' in result
        assert 'p_value' in result
        assert 'normal' in result
    
    def test_regression_analysis_linear(self, correlation_data):
        """Test linear regression analysis."""
        analyzer = DataAnalyzer(correlation_data)
        result = analyzer.regression_analysis('var1', ['var2', 'var3', 'var4'])
        
        assert result['method'] == 'linear_regression'
        assert 'r2_score' in result
        assert 'mse' in result
        assert 'rmse' in result
        assert 'mae' in result
        assert 'intercept' in result
        assert 'coefficients' in result
        assert 'feature_columns' in result
        assert 'target_column' in result
        assert 'n_samples' in result
        assert 'predictions' in result
    
    def test_regression_analysis_auto_features(self, correlation_data):
        """Test regression analysis with automatic feature selection."""
        analyzer = DataAnalyzer(correlation_data)
        result = analyzer.regression_analysis('var1')
        
        assert result['method'] == 'linear_regression'
        assert 'feature_columns' in result
        assert len(result['feature_columns']) > 0
    
    def test_anova_analysis(self, sample_dataframe):
        """Test ANOVA analysis."""
        analyzer = DataAnalyzer(sample_dataframe)
        result = analyzer.anova_analysis('numeric_col', 'categorical_col')
        
        assert result['test_type'] == 'one_way_anova'
        assert 'f_statistic' in result
        assert 'p_value' in result
        assert 'significant' in result
        assert 'groups' in result
        assert 'group_statistics' in result
        assert 'columns' in result
    
    def test_get_summary_report(self, sample_dataframe):
        """Test getting comprehensive summary report."""
        analyzer = DataAnalyzer(sample_dataframe)
        
        # Perform some analyses
        analyzer.get_descriptive_stats()
        analyzer.get_correlation_matrix()
        
        report = analyzer.get_summary_report()
        
        assert 'data_info' in report
        assert 'analyses_performed' in report
        assert 'results' in report
        assert len(report['analyses_performed']) > 0
    
    def test_export_results_json(self, sample_dataframe, temp_file):
        """Test exporting results as JSON."""
        analyzer = DataAnalyzer(sample_dataframe)
        
        # Perform some analyses
        analyzer.get_descriptive_stats()
        analyzer.get_correlation_matrix()
        
        output_path = temp_file.replace('.csv', '_results.json')
        result = analyzer.export_results(output_path, format='json')
        
        assert result is analyzer  # Method chaining
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
    
    def test_export_results_csv(self, sample_dataframe, temp_file):
        """Test exporting results as CSV."""
        analyzer = DataAnalyzer(sample_dataframe)
        
        # Perform descriptive statistics
        analyzer.get_descriptive_stats()
        
        output_path = temp_file.replace('.csv', '_results.csv')
        result = analyzer.export_results(output_path, format='csv')
        
        assert result is analyzer
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
    
    def test_export_results_excel(self, sample_dataframe, temp_file):
        """Test exporting results as Excel."""
        analyzer = DataAnalyzer(sample_dataframe)
        
        # Perform analyses
        analyzer.get_descriptive_stats()
        analyzer.get_correlation_matrix()
        
        output_path = temp_file.replace('.csv', '_results.xlsx')
        result = analyzer.export_results(output_path, format='excel')
        
        assert result is analyzer
        assert os.path.exists(output_path)
        
        # Cleanup
        if os.path.exists(output_path):
            os.unlink(output_path)
    
    def test_error_handling_no_data(self):
        """Test error handling when no data is loaded."""
        analyzer = DataAnalyzer()
        
        with pytest.raises(ValueError):
            analyzer.get_descriptive_stats()
        
        with pytest.raises(ValueError):
            analyzer.get_correlation_matrix()
        
        with pytest.raises(ValueError):
            analyzer.hypothesis_test('ttest', column1='col1')
    
    def test_error_handling_invalid_test_type(self, sample_dataframe):
        """Test error handling with invalid test type."""
        analyzer = DataAnalyzer(sample_dataframe)
        
        with pytest.raises(ValueError):
            analyzer.hypothesis_test('invalid_test')
    
    def test_error_handling_invalid_normality_test(self, sample_dataframe):
        """Test error handling with invalid normality test."""
        analyzer = DataAnalyzer(sample_dataframe)
        
        with pytest.raises(ValueError):
            analyzer.hypothesis_test('normality', column='numeric_col', test='invalid')
    
    def test_error_handling_invalid_regression_method(self, sample_dataframe):
        """Test error handling with invalid regression method."""
        analyzer = DataAnalyzer(sample_dataframe)
        
        with pytest.raises(ValueError):
            analyzer.regression_analysis('numeric_col', method='invalid')
    
    def test_error_handling_insufficient_data_correlation(self, mock_data):
        """Test error handling with insufficient data for correlation."""
        analyzer = DataAnalyzer(mock_data['single_col_df'])
        
        result = analyzer.get_correlation_matrix()
        assert 'error' in result
    
    def test_error_handling_insufficient_data_anova(self, mock_data):
        """Test error handling with insufficient data for ANOVA."""
        analyzer = DataAnalyzer(mock_data['single_col_df'])
        
        result = analyzer.anova_analysis('col1', 'col1')
        assert 'error' in result
    
    def test_error_handling_insufficient_data_kruskal(self, mock_data):
        """Test error handling with insufficient data for Kruskal-Wallis."""
        analyzer = DataAnalyzer(mock_data['single_col_df'])
        
        result = analyzer.hypothesis_test('kruskal', value_column='col1', group_column='col1')
        assert 'error' in result
    
    def test_error_handling_insufficient_data_regression(self, mock_data):
        """Test error handling with insufficient data for regression."""
        analyzer = DataAnalyzer(mock_data['single_col_df'])
        
        result = analyzer.regression_analysis('col1')
        assert 'error' in result
    
    def test_series_handling(self, sample_series):
        """Test handling of pandas Series."""
        analyzer = DataAnalyzer(sample_series)
        
        # Should work with Series
        stats = analyzer.get_descriptive_stats()
        assert len(stats) > 0
    
    def test_empty_dataframe(self, mock_data):
        """Test handling of empty DataFrame."""
        analyzer = DataAnalyzer(mock_data['empty_df'])
        
        # Should handle empty DataFrame gracefully
        stats = analyzer.get_descriptive_stats()
        assert 'error' in stats
    
    def test_all_nan_dataframe(self, mock_data):
        """Test handling of DataFrame with all NaN values."""
        analyzer = DataAnalyzer(mock_data['all_nan_df'])
        
        # Should handle all NaN DataFrame
        stats = analyzer.get_descriptive_stats()
        # Should return empty dict or error
        assert isinstance(stats, dict)
    
    def test_mixed_types_dataframe(self, mock_data):
        """Test handling of DataFrame with mixed data types."""
        analyzer = DataAnalyzer(mock_data['mixed_types_df'])
        
        # Should work with mixed types
        stats = analyzer.get_descriptive_stats()
        assert len(stats) > 0
        
        # Should only include numeric columns in correlation
        corr = analyzer.get_correlation_matrix()
        assert 'correlation_matrix' in corr or 'error' in corr
    
    def test_comprehensive_analysis_pipeline(self, correlation_data):
        """Test a comprehensive analysis pipeline."""
        analyzer = DataAnalyzer(correlation_data)
        
        # Perform multiple analyses
        desc_stats = analyzer.get_descriptive_stats()
        corr_matrix = analyzer.get_correlation_matrix()
        regression = analyzer.regression_analysis('var1', ['var2', 'var3'])
        anova = analyzer.anova_analysis('var1', 'category')
        
        # Check that all analyses were performed
        assert len(desc_stats) > 0
        assert 'correlation_matrix' in corr_matrix
        assert regression['method'] == 'linear_regression'
        assert anova['test_type'] == 'one_way_anova'
        
        # Get summary report
        report = analyzer.get_summary_report()
        assert len(report['analyses_performed']) >= 4
    
    def test_analysis_results_storage(self, sample_dataframe):
        """Test that analysis results are stored correctly."""
        analyzer = DataAnalyzer(sample_dataframe)
        
        # Perform analyses
        desc_stats = analyzer.get_descriptive_stats()
        corr_matrix = analyzer.get_correlation_matrix()
        
        # Check that results are stored
        assert 'descriptive_stats' in analyzer.analysis_results
        assert 'correlation' in analyzer.analysis_results
        
        # Check that stored results match returned results
        assert analyzer.analysis_results['descriptive_stats'] == desc_stats
        assert analyzer.analysis_results['correlation'] == corr_matrix
