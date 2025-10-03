qemu.qmp File Index
===================

This file is here to explain the purpose of all the little bits and
pieces of project files in the root directory and how they are
used. It's useful info for those contributing to this project, but not
so much for those who just want to use the library.


Much ado about packaging
------------------------

``pyproject.toml`` defines the build backend and build dependencies.
This project uses the ``setuptools.build_meta`` build backend.
The backend reads the packaging configuration from ``setup.cfg``.
Other than ``setuptools``, this package requires ``setuptools_scm`` at
buildtime to determine the package version based on git metadata.

1. ``pip3 install .`` will install these packages to your current
   environment. If you are inside a virtual environment, they will
   install there. If you are not, it will attempt to install to the
   global environment, which is **not recommended**.

2. ``pip3 install --user .`` will install these packages to your user's
   local python packages. If you are inside of a virtual environment,
   this will fail; you want the first invocation above.

If you append the ``--editable`` or ``-e`` argument to either invocation
above, pip will install in "editable" mode. This installs the package as
a forwarder that points to the source tree. In so
doing, the installed package always reflects the latest version in your
source tree.
This feature requires pip 21.3 or newer.
See `Development Mode (a.k.a. “Editable Installs”)
<https://setuptools.pypa.io/en/latest/userguide/development_mode.html>`_
in the Setuptools documentation for more information.

Installing ".[devel]" instead of "." will additionally pull in required
packages for testing this package. They are not runtime requirements,
and are not needed to simply use these libraries.

Running ``make develop`` will pull in all testing dependencies and
install QEMU in editable mode to the current environment.
(It is a shortcut for ``pip3 install -e .[devel]``.)

See `Installing packages using pip and virtual environments
<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>`_
for more information.


Files in this directory
-----------------------

- ``qemu/`` Python 'qemu' namespace package source directory.
- ``tests/`` Python package tests directory.
- ``.gitlab-ci.d/`` Files used for GitLab CI configuration.
- ``.gitlab-ci.yml`` Primary GitLab CI configuration file.
- ``FILES.rst`` you are here!
- ``LICENSE`` This project is licensed as LGPLv2+; except for
  ``legacy.py``.
- ``LICENSE_GPL2`` This is the license for ``legacy.py``.
- ``Makefile`` provides some common testing/installation invocations.
  Try ``make help`` to see available targets.
- ``MANIFEST.in`` is read by python setuptools, it specifies additional files
  that should be included by a source distribution.
- ``README.rst`` is used as the README file that is visible on PyPI.org.
- ``setup.cfg`` houses setuptools package configuration.
- ``setup.py`` is the setuptools installer used by pip; See above.
