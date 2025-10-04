Quick Start Guide
=================

This guide will get you up and running with DataX in just a few minutes.

Installation
------------

First, install DataX:

.. code-block:: bash

   pip install datax

Basic Usage
-----------

Let's start with a simple example using sample data:

.. code-block:: python

   import pandas as pd
   import numpy as np
   from datax import DataCleaner, DataAnalyzer, DataVisualizer

   # Create sample data
   np.random.seed(42)
   data = {
       'age': np.random.randint(18, 80, 100),
       'salary': np.random.normal(50000, 15000, 100),
       'department': np.random.choice(['IT', 'HR', 'Finance'], 100),
       'score': np.random.uniform(0, 100, 100)
   }
   
   # Add some missing values and outliers
   data['age'][10:15] = np.nan
   data['salary'][0] = 1000000  # Outlier
   
   df = pd.DataFrame(data)
   print("Original data shape:", df.shape)
   print("Missing values:", df.isnull().sum().sum())

Data Cleaning
-------------

Clean your data with DataX:

.. code-block:: python

   # Initialize cleaner
   cleaner = DataCleaner(df)
   
   # Handle missing values automatically
   cleaner.handle_missing_values(method='auto')
   
   # Remove duplicate rows
   cleaner.remove_duplicates()
   
   # Handle outliers by capping them
   cleaner.handle_outliers(method='iqr', action='cap')
   
   # Convert data types automatically
   cleaner.convert_data_types(auto_convert=True)
   
   # Get cleaned data
   cleaned_data = cleaner.data
   print("Cleaned data shape:", cleaned_data.shape)
   print("Missing values after cleaning:", cleaned_data.isnull().sum().sum())

Statistical Analysis
--------------------

Analyze your cleaned data:

.. code-block:: python

   # Initialize analyzer
   analyzer = DataAnalyzer(cleaned_data)
   
   # Get descriptive statistics
   desc_stats = analyzer.get_descriptive_stats()
   print("Descriptive statistics:")
   for col, stats in desc_stats.items():
       print(f"{col}: mean={stats['mean']:.2f}, std={stats['std']:.2f}")
   
   # Calculate correlation matrix
   correlation = analyzer.get_correlation_matrix()
   print("\nStrong correlations found:")
   for corr in correlation['strong_correlations']:
       print(f"{corr['var1']} - {corr['var2']}: {corr['correlation']:.3f}")
   
   # Perform regression analysis
   regression = analyzer.regression_analysis('salary', ['age', 'score'])
   print(f"\nRegression R² score: {regression['r2_score']:.3f}")

Data Visualization
------------------

Create visualizations:

.. code-block:: python

   # Initialize visualizer
   visualizer = DataVisualizer(cleaned_data, style='colorful')
   
   # Plot distributions
   visualizer.plot_distribution('age', plot_type='histogram', kde=True)
   visualizer.plot_distribution('salary', plot_type='box')
   
   # Plot correlation heatmap
   visualizer.plot_correlation_heatmap(annot=True)
   
   # Plot multiple distributions
   visualizer.plot_multiple_distributions(['age', 'salary', 'score'])
   
   # Show all plots
   visualizer.show_all_plots()

Command Line Interface
----------------------

You can also use DataX from the command line:

.. code-block:: bash

   # Save your data first
   df.to_csv('sample_data.csv', index=False)
   
   # Load and analyze data
   datax load sample_data.csv info
   
   # Clean data
   datax load sample_data.csv clean --missing auto --remove-duplicates
   
   # Perform statistical analysis
   datax load sample_data.csv stats --descriptive --correlation
   
   # Create visualizations
   datax load sample_data.csv viz --distributions --correlation-heatmap

Interactive Mode
----------------

Start interactive mode for exploratory data analysis:

.. code-block:: bash

   datax interactive --file sample_data.csv

In interactive mode, you can:

* Load different datasets
* Perform cleaning operations
* Run statistical analyses
* Create visualizations
* Get help with commands

Advanced Features
-----------------

Data Validation
~~~~~~~~~~~~~~~

Define custom validation rules:

.. code-block:: python

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
       }
   }
   
   validation_results = cleaner.validate_data(rules=validation_rules)
   print("Validation passed:", validation_results['passed'])

Hypothesis Testing
~~~~~~~~~~~~~~~~~~

Perform various hypothesis tests:

.. code-block:: python

   # T-test
   ttest_result = analyzer.hypothesis_test('ttest', 
                                         column1='age', 
                                         column2='score')
   print("T-test p-value:", ttest_result['p_value'])
   
   # Normality test
   normality_result = analyzer.hypothesis_test('normality', 
                                             column='salary', 
                                             test='shapiro')
   print("Data is normal:", normality_result['normal'])

Interactive Visualizations
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create interactive plots with Plotly:

.. code-block:: python

   # Interactive scatter plot
   interactive_fig = visualizer.create_interactive_plot('scatter',
                                                       x_column='age',
                                                       y_column='salary',
                                                       color_column='department')
   
   # Save interactive plot
   visualizer.save_plot(interactive_fig, 'interactive_plot.html', format='html')

Export Results
~~~~~~~~~~~~~~

Export your analysis results:

.. code-block:: python

   # Export statistical results
   analyzer.export_results('analysis_results.json', format='json')
   
   # Save cleaned data
   cleaner.save_cleaned_data('cleaned_data.csv', format='csv')
   
   # Save plots
   visualizer.save_plot(fig, 'distribution_plot.png', format='png', dpi=300)

Next Steps
----------

Now that you've completed the quick start:

1. Read the :ref:`user_guide` for detailed usage
2. Explore the :ref:`api_reference` for all available functions
3. Check out the :ref:`examples` for more complex use cases
4. Join our community for support and discussions

Happy analyzing with DataX! 🚀
