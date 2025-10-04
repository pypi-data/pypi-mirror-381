.. _installation:

============
Installation
============

*TL;DR*: end users only need:

.. code-block:: console

  pip install pyRugged

→ it will install the latest stable release from `PyPI <https://pypi.org/project/pyRugged/>`_.


Pre requisites
--------------

Virtual environement with `orekit-jcc <https://gitlab.eopf.copernicus.eu/geolib/orekit-jcc>`_

.. code-block:: console

  python -m venv .venv
  . .venv/bin/activate
  python -m pip install orekit-jcc


Installation from source
------------------------

.. code-block:: console

  pip install -e .


For developpers
---------------

Upgrade pip ``>=25.1`` to add support for
`Dependency Groups <https://pip.pypa.io/en/stable/user_guide/#dependency-groups>`_
(`PEP 735 <https://peps.python.org/pep-0735/>`_)

.. code-block:: console

  pip install --upgrade pip


* to install dev dependencies

.. code-block:: console

  pip install -e . --group dev

* to run notebook

.. code-block:: console

  pip install -e . --group notebook

* to build doc: see
  `README <https://gitlab.eopf.copernicus.eu/geolib/pyrugged/-/blob/main/docs/README.md>`_
  in docs repository
