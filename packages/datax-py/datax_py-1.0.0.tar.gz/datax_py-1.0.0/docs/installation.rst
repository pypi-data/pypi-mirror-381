Installation
============

DataX can be installed using pip, conda, or from source.

Prerequisites
-------------

DataX requires Python 3.8 or higher. The following packages are required:

* pandas >= 1.3.0
* numpy >= 1.21.0
* matplotlib >= 3.5.0
* seaborn >= 0.11.0
* scipy >= 1.7.0
* scikit-learn >= 1.0.0
* plotly >= 5.0.0

Installation Methods
--------------------

From PyPI (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~

The easiest way to install DataX is using pip:

.. code-block:: bash

   pip install datax

From Conda
~~~~~~~~~~

DataX is available on conda-forge:

.. code-block:: bash

   conda install -c conda-forge datax

From Source
~~~~~~~~~~~

To install from source:

.. code-block:: bash

   git clone https://github.com/datax/datax.git
   cd datax
   pip install -e .

Development Installation
~~~~~~~~~~~~~~~~~~~~~~~~

For development, install with development dependencies:

.. code-block:: bash

   git clone https://github.com/datax/datax.git
   cd datax
   pip install -e ".[dev]"

Optional Dependencies
---------------------

DataX provides optional dependencies for enhanced functionality:

Development Tools
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install datax[dev]

Includes:
* pytest and pytest-cov for testing
* black, flake8, mypy for code quality
* pre-commit for git hooks

Documentation
~~~~~~~~~~~~~

.. code-block:: bash

   pip install datax[docs]

Includes:
* sphinx for documentation generation
* sphinx-rtd-theme for documentation theme

Jupyter Integration
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install datax[jupyter]

Includes:
* jupyter for notebook support
* ipywidgets for interactive widgets

All Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install datax[all]

Verification
------------

To verify the installation, run:

.. code-block:: python

   import datax
   print(datax.__version__)

Or from the command line:

.. code-block:: bash

   datax --version

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

ImportError: No module named 'datax'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This usually means DataX is not installed or not in your Python path. Try:

.. code-block:: bash

   pip install --upgrade datax

Permission Denied
^^^^^^^^^^^^^^^^^

If you get permission errors, try installing with user flag:

.. code-block:: bash

   pip install --user datax

Or use a virtual environment:

.. code-block:: bash

   python -m venv datax_env
   source datax_env/bin/activate  # On Windows: datax_env\Scripts\activate
   pip install datax

Version Conflicts
^^^^^^^^^^^^^^^^^

If you encounter version conflicts, try:

.. code-block:: bash

   pip install --upgrade datax
   pip install --upgrade pandas numpy matplotlib seaborn scipy scikit-learn plotly

Getting Help
------------

If you encounter issues:

1. Check the :ref:`troubleshooting` section
2. Search existing `GitHub issues <https://github.com/datax/datax/issues>`_
3. Create a new issue with detailed information
4. Join our `Discord community <https://discord.gg/datax>`_

System Requirements
-------------------

Minimum Requirements
~~~~~~~~~~~~~~~~~~~~

* Python 3.8+
* 2GB RAM
* 1GB disk space

Recommended Requirements
~~~~~~~~~~~~~~~~~~~~~~~~

* Python 3.10+
* 8GB RAM
* 10GB disk space
* SSD storage for better performance

Supported Platforms
~~~~~~~~~~~~~~~~~~~

* Windows 10/11
* macOS 10.15+
* Linux (Ubuntu 18.04+, CentOS 7+, RHEL 7+)

Docker Installation
-------------------

DataX is also available as a Docker image:

.. code-block:: bash

   docker pull datax/datax:latest
   docker run -it datax/datax:latest

For development with Jupyter:

.. code-block:: bash

   docker run -p 8888:8888 datax/datax:jupyter
