=======================
Ubuntu Package Download
=======================


.. image:: https://img.shields.io/pypi/v/ubuntu_package_download.svg
        :target: https://pypi.python.org/pypi/ubuntu_package_download

.. image:: https://img.shields.io/travis/philroche/ubuntu_package_download.svg
        :target: https://travis-ci.com/philroche/ubuntu_package_download

.. image:: https://readthedocs.org/projects/ubuntu-package-download/badge/?version=latest
        :target: https://ubuntu-package-download.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

Helpful utility to download Ubuntu debian packages

Process/Order of finding the package and fallback logic:

    1. Attempt to find the package in the specified series and architecture
    2. If the package is not found in the specified series and architecture attempt to find the package in the `all` architecture (amd64)
    3. If the package is not found in the `all` architecture attempt to find the package in a previous series if the `fallback_series` flag is set to True
    4. If the package is not found in a previous series attempt to find the previous version of the package in the same series if the `fallback_version` flag is set to True

    If not found in any of the above steps log an error message to the console.

Usage: :code:`poetry install` will setup the tool to be used locally. You should then be able to use the tool by invoking :code:`poetry run ubuntu-package-download [args]` or :code:`ubuntu-package-download [args]`.

* Free software: GNU General Public License v3
* Documentation: https://ubuntu-package-download.readthedocs.io.


Features
--------

* TODO

Development
-----------

This project uses poetry for dependency management.

To make sure dev dependencies are installed use :code:`poetry install --with dev`. If you are a developer of this tool use :code:`poetry run ubuntu-package-download [args]` or :code:`ubuntu-package-download` inside :code:`poetry shell` as this will pickup any changes you make to the code.

For more information see: `Poetry Basic Usage`_

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Poetry Basic Usage: https://python-poetry.org/docs/basic-usage/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
