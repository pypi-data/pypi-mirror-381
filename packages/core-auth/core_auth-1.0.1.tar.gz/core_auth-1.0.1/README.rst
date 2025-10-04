core-auth
===============================================================================

This project/library contains common elements related to 
authentication & authorization...

===============================================================================

.. image:: https://img.shields.io/pypi/pyversions/core-auth.svg
    :target: https://pypi.org/project/core-auth/
    :alt: Python Versions

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://gitlab.com/bytecode-solutions/core/core-auth/-/blob/main/LICENSE
    :alt: License

.. image:: https://gitlab.com/bytecode-solutions/core/core-auth/badges/release/pipeline.svg
    :target: https://gitlab.com/bytecode-solutions/core/core-auth/-/pipelines
    :alt: Pipeline Status

.. image:: https://readthedocs.org/projects/core-auth/badge/?version=latest
    :target: https://readthedocs.org/projects/core-auth/
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


Current implementations
---------------------------------------

JwtToken
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a wrapper to simplify the encoding and
decoding process for JWT tokens using PyJWT library.

Example...

.. code-block:: python

    # -*- coding: utf-8 -*-

    from core_auth.auth.jwt_token.jwt_auth import JwtToken

    client = JwtToken(private_key="S3cr3t")
    token = client.encode(subject="SomeSubject")
    print(client.decode(token))
..
