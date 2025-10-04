# DataX - Advanced Data Analytics Package

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/datax-py.svg)](https://pypi.org/project/datax-py/)
[![Downloads](https://pepy.tech/badge/datax-py)](https://pepy.tech/project/datax-py)
[![Build Status](https://github.com/amirbekazimov/datax-py/workflows/CI/badge.svg)](https://github.com/amirbekazimov/datax-py/actions)
[![Coverage](https://codecov.io/gh/amirbekazimov/datax-py/branch/main/graph/badge.svg)](https://codecov.io/gh/amirbekazimov/datax-py)
[![Documentation Status](https://readthedocs.org/projects/datax-py/badge/?version=latest)](https://datax-py.readthedocs.io/en/latest/?badge=latest)

**DataX** is a comprehensive Python package for data analytics that provides powerful tools for data cleaning, statistical analysis, and visualization. Built with modern Python practices, it offers both programmatic and command-line interfaces for maximum flexibility.

## 🚀 Features

### Core Functionality
- **Advanced Data Cleaning**: Missing value handling, outlier detection, data validation, type conversion
- **Comprehensive Statistics**: Descriptive statistics, correlation analysis, hypothesis testing, regression analysis
- **Rich Visualizations**: Statistical plots, interactive charts, customizable themes, export capabilities
- **Command Line Interface**: Full CLI support with interactive mode and batch processing
- **High Performance**: Optimized for large datasets with efficient memory usage

### Advanced Features
- **Interactive Mode**: Jupyter notebook integration and interactive plotting
- **Statistical Modeling**: Linear regression, ANOVA, normality testing
- **Data Validation**: Custom rule-based validation with comprehensive reporting
- **Export Capabilities**: Multiple output formats (CSV, Excel, JSON, Parquet)
- **Extensible Architecture**: Plugin system for custom analyzers and visualizers

## 📦 Installation

### From PyPI (Recommended)
```bash
pip install datax-py
```

### From Source
```bash
git clone https://github.com/amirbekazimov/datax-py.git
cd datax-py
pip install -e .
```

### With Optional Dependencies
```bash
# For development
pip install datax-py[dev]

# For documentation
pip install datax-py[docs]

# For Jupyter integration
pip install datax[jupyter]

# All optional dependencies
pip install datax[all]
```

## 🎯 Quick Start

### Python API

```python
import pandas as pd
from datax import DataCleaner, DataAnalyzer, DataVisualizer

# Load your data
df = pd.read_csv('your_data.csv')

# Data Cleaning
cleaner = DataCleaner(df)
cleaner.handle_missing_values(method='auto')
cleaner.remove_duplicates()
cleaner.handle_outliers(method='iqr', action='cap')
cleaned_data = cleaner.data

# Statistical Analysis
analyzer = DataAnalyzer(cleaned_data)
desc_stats = analyzer.get_descriptive_stats()
correlation = analyzer.get_correlation_matrix()
regression = analyzer.regression_analysis('target_column', ['feature1', 'feature2'])

# Visualization
visualizer = DataVisualizer(cleaned_data)
visualizer.plot_distribution('column_name')
visualizer.plot_correlation_heatmap()
visualizer.plot_multiple_distributions(['col1', 'col2', 'col3'])
```

### Command Line Interface

```bash
# Load data and get information
datax load data.csv info

# Clean data with auto missing value handling
datax load data.csv clean --missing auto --remove-duplicates

# Perform statistical analysis
datax load data.csv stats --descriptive --correlation

# Create visualizations
datax load data.csv viz --distributions --correlation-heatmap

# Interactive mode
datax interactive --file data.csv
```

## 📊 Examples

### Data Cleaning Pipeline

```python
from datax import DataCleaner
import pandas as pd

# Load data
df = pd.read_csv('messy_data.csv')

# Initialize cleaner
cleaner = DataCleaner(df)

# Comprehensive cleaning pipeline
cleaner.handle_missing_values(method='auto') \
       .remove_duplicates() \
       .handle_outliers(method='iqr', action='cap') \
       .convert_data_types(auto_convert=True) \
       .validate_data()

# Get cleaning summary
summary = cleaner.get_cleaning_summary()
print(f"Original shape: {summary['original_shape']}")
print(f"Final shape: {summary['current_shape']}")

# Save cleaned data
cleaner.save_cleaned_data('cleaned_data.csv')
```

### Statistical Analysis

```python
from datax import DataAnalyzer

analyzer = DataAnalyzer(df)

# Descriptive statistics
desc_stats = analyzer.get_descriptive_stats()

# Correlation analysis
correlation = analyzer.get_correlation_matrix(method='pearson')

# Hypothesis testing
ttest_result = analyzer.hypothesis_test('ttest', 
                                       column1='group1', 
                                       column2='group2')

# Regression analysis
regression = analyzer.regression_analysis('target', 
                                        ['feature1', 'feature2', 'feature3'])

# ANOVA analysis
anova = analyzer.anova_analysis('value_column', 'group_column')

# Export results
analyzer.export_results('analysis_results.json')
```

### Advanced Visualizations

```python
from datax import DataVisualizer

visualizer = DataVisualizer(df, style='colorful')

# Distribution plots
visualizer.plot_distribution('numeric_column', plot_type='histogram', kde=True)

# Correlation heatmap
visualizer.plot_correlation_heatmap(annot=True)

# Multiple distributions
numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
visualizer.plot_multiple_distributions(numeric_cols[:6])

# Interactive plots
interactive_fig = visualizer.create_interactive_plot('scatter',
                                                   x_column='x',
                                                   y_column='y',
                                                   color_column='category')

# Save plots
visualizer.save_plot(fig, 'output.png', format='png', dpi=300)
```

## 🛠️ CLI Usage

### Basic Commands

```bash
# Show help
datax --help

# Load and analyze data
datax load data.csv info
datax load data.csv clean --missing auto
datax load data.csv stats --descriptive --correlation
datax load data.csv viz --distributions --correlation-heatmap

# Interactive mode
datax interactive --file data.csv
```

### Advanced CLI Features

```bash
# Batch processing
datax batch config.json

# Custom output formats
datax load data.csv clean --output cleaned_data.xlsx --format excel

# Verbose output
datax load data.csv stats --descriptive --verbose

# Save plots
datax load data.csv viz --distributions --save-plots ./plots/
```

## 📈 Performance

DataX is optimized for performance with large datasets:

- **Memory Efficient**: Uses pandas' efficient data structures
- **Vectorized Operations**: Leverages NumPy and pandas vectorization
- **Lazy Evaluation**: Computes statistics only when needed
- **Parallel Processing**: Supports multiprocessing for large datasets
- **Caching**: Intelligent caching of computed results

## 🔧 Configuration

### Custom Themes and Styles

```python
# Set custom visualization style
visualizer = DataVisualizer(df, style='dark')
visualizer.set_style('minimal')

# Custom color palettes
import seaborn as sns
sns.set_palette("Set2")
```

### Advanced Configuration

```python
# Custom validation rules
validation_rules = {
    "age_range": {
        "type": "range",
        "column": "age",
        "min": 0,
        "max": 120
    },
    "unique_id": {
        "type": "unique",
        "column": "id"
    }
}

cleaner.validate_data(rules=validation_rules, strict=True)
```

## 📚 Documentation

- [Full Documentation](https://datax-py.readthedocs.io)
- [API Reference](https://datax-py.readthedocs.io/en/latest/api.html)
- [Examples Gallery](https://datax-py.readthedocs.io/en/latest/examples.html)
- [Contributing Guide](CONTRIBUTING.md)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/amirbekazimov/datax-py.git
cd datax-py
pip install -e ".[dev]"
pre-commit install
pytest
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=datax --cov-report=html

# Run specific test categories
pytest -m "not slow"
pytest -m integration
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on top of the amazing [pandas](https://pandas.pydata.org/) library
- Visualization powered by [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/)
- Statistical functions from [scipy](https://scipy.org/) and [scikit-learn](https://scikit-learn.org/)
- Interactive plots with [plotly](https://plotly.com/python/)

## 📞 Support

- **Documentation**: [https://datax-py.readthedocs.io](https://datax-py.readthedocs.io)
- **Issues**: [GitHub Issues](https://github.com/amirbekazimov/datax-py/issues)
- **Discussions**: [GitHub Discussions](https://github.com/amirbekazimov/datax-py/discussions)
- **Email**: [amirbekazimov7@gmail.com](mailto:amirbekazimov7@gmail.com)

## 🗺️ Roadmap

- [ ] Machine learning integration
- [ ] Time series analysis
- [ ] Geospatial data support
- [ ] Web dashboard interface
- [ ] Real-time data processing
- [ ] Cloud deployment support

---

**DataX** - Making data analytics accessible, powerful, and enjoyable! 🚀
