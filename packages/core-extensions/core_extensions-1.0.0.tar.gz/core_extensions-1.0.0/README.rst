# core-extensions
===============================================================================

This project contains common elements for different
projects. Unlike `core-mixins`, this project requires external
dependencies...

===============================================================================

.. image:: https://img.shields.io/pypi/pyversions/core-extensions.svg
    :target: https://pypi.org/project/core-extensions/
    :alt: Python Versions

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://gitlab.com/bytecode-solutions/core/core-extensions/-/blob/main/LICENSE
    :alt: License

.. image:: https://gitlab.com/bytecode-solutions/core/core-extensions/badges/release/pipeline.svg
    :target: https://gitlab.com/bytecode-solutions/core/core-extensions/-/pipelines
    :alt: Pipeline Status

.. image:: https://readthedocs.org/projects/core-extensions/badge/?version=latest
    :target: https://readthedocs.org/projects/core-extensions/
    :alt: Docs Status

.. image:: https://img.shields.io/badge/security-bandit-yellow.svg
    :target: https://github.com/PyCQA/bandit
    :alt: Security

|

Execution Environment
---------------------------------------

Install libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    pip install --upgrade pip
    pip install virtualenv
..

Create the Python Virtual Environment.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    virtualenv --python={{python-version}} .venv
    virtualenv --python=python3.11 .venv
..

Activate the Virtual Environment.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    source .venv/bin/activate
..

Install required libraries.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    pip install .
..

Check tests and coverage.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    python manager.py run-tests
    python manager.py run-coverage
..
