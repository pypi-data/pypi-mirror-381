.. include:: links.inc

Installing
==========


Requirements
^^^^^^^^^^^^

hipsnp requires the following packages:

* datalad>=0.14.0
* pandas>=1.1.2
* numpy>=1.16
* bgen_reader>=4.0.8

Additionally, hipsnp requires that QCTOOL is installed: 
https://www.well.ox.ac.uk/~gav/qctool/documentation/download.html

Running the examples requires:

Depending on the installation method, this packages might be installed
automatically.

Installing
^^^^^^^^^^
There are different ways to install hipsnp:

* Install the :ref:`install_latest_release`. This is the most suitable approach
  for most end users.
* Install the :ref:`install_latest_development`. This version will have the
  latest features. However, it is still under development and not yet
  officially released. Some features might still change before the next stable
  release.
* Install from :ref:`install_development_git`. This is mostly suitable for
  developers that want to have the latest version and yet edit the code.


Either way, we strongly recommend using virtual environments:

* `venv`_
* `conda env`_


.. _install_latest_release:

Latest release
--------------

We have packaged hipsnp and published it in PyPi, so you can just install it
with `pip`.

.. code-block:: bash

    pip install -U hipsnp


.. _install_latest_development:

Latest Development Version
--------------------------
First, make sure that you have all the dependencies installed:

Then, install hipsnp from TestPypi

.. code-block:: bash

    pip install --index-url https://test.pypi.org/simple/ -U hipsnp --pre


.. _install_development_git:

Local git repository (for developers)
-------------------------------------
First, make sure that you have all the dependencies installed:

Then, clone `hipsnp Github`_ repository in a folder of your choice:

.. code-block:: bash

    git clone https://github.com/juaml/hipsnp/

Install development mode requirements:

.. code-block:: bash

    cd hipsnp
    pip install -r dev-requirements.txt

Finally, install in development mode:

.. code-block:: bash

    python setup.py develop

.. note:: Every time that you run ``setup.py develop``, the version is going to
  be automatically set based on the git history. Nevertheless, this change 
  should not be committed (changes to ``_version.py``). Running ``git stash``
  at this point will forget the local changes to ``_version.py``.
