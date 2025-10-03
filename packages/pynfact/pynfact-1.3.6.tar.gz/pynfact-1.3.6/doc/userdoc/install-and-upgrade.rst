.. vim: set ft=rst fenc=utf-8 tw=72 nowrap:

*******************
Install and upgrade
*******************

Installing
==========

Using ``pip``
-------------

PynFact requires Python 3.6+.  You may install it by running the
following command in any terminal::

    pip install pynfact

In some systems where Python 2 is the default version, it's possible
that the installed for Python 3 is called ``pip3``.  Either way, you may
run ``pip`` by invoking ``python`` directly::

    python3 -m pip install pynfact

This will install ``pynfact`` to your local system.  In case of wanting
``pynfact`` system-wide, i.e., available to all users, run the command as
``root`` or use ``sudo``::

    sudo pip install pynfact

Downloading the source
----------------------

Pynfact require some dependencies in order to work, so make sure that
the following packages are on your system:

* ``docutils``: Python Documentation Utilities
* ``feedgen``: Feed Generator (Atom, RSS, Podcasts)
* ``Jinja2`` : A small but fast and easy to use stand-alone template
  engine written in pure Python
* ``markdown``: Python implementation of Markdown
* ``python-dateutil``: Extensions to the standard Python datetime module
* ``unidecode``: ASCII transliterations of Unicode text

Download the project source, either from `GitHub`_ or from `PyPI`_.
Once you have uncompressed the tarball, you may run::

    python setup.py install

Upgrading
=========

Using ``pip``
-------------

If you have installed PynFact by using ``pip`` and want to upgrade to
the latest stable release, you may do it by using the option
``--upgrade`` in the ``pip`` command::

    pip install --upgrade pynfact

Directly by source
------------------

In case of having used the source tarball, just repeat the installation
process with the latest stable version.


.. _GitHub: https://github.com/jacorbal/pynfact
.. _PyPI: https://pypi.org/project/pynfact/#files
