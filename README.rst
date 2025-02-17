RF Surveillance 

Radio Frequency Surveillance Center which receive alarm from different nodes 

------

.. start-badges see https://shields.io/badges and collection see https://github.com/inttter/md-badges

| |build| |release_version| |wheel| |supported_versions|
| |docs| |pylint| |docs_pass|
| |ruff| |gh-lic| |commits_since_specific_tag_on_main| |commits_since_latest_github_release|


|
| **Code:** https://github.com/alanmehifo/rf-surveillance
| **Docs:** https://rf-surveillance.readthedocs.io/en/latest/
| **PyPI:** https://pypi.org/project/rf-surveillance/
| **CI:** https://github.com/alanmehio/rf-surveillance/actions/
  
|
|
| |dmc_image|

|dmc_gif|

Features
========

1. **dmcview** `python package`

   a. View Object Azimuth, Inclindation(Elevation) and Bank; also View Declination(Offset from real North)  
   b. View animation to reflect real DMC device in 2D. Acceleration is not implemented yet 
2. Tested against Linux(ubuntu-latest) `platforms` and `python` 3.12.3
3. See `TODO <https://github.com/alammehio/rf-surveillance/blob/master/TODO.rst>`_.

Technical Debt
==============
See `Technical Debt <https://github.com/alammehio/rf-surveillance/blob/master/TECHNICALDEBT.rst>`_.

Change Log
==========
 `Change Log <https://github.com/alammehio/rf-surveillance/blob/master/CHANGELOG.rst>`_.

How to Contribute
=================
 `Contribute <https://github.com/alammehio/rf-surveillance/blob/master/CONTRIBUTING.md>`_.

Development
===========
| `Development <https://github.com/alammehio/rf-surveillance/blob/master/docs/source/contents/development.rst>`_.

Quickstart
==========
| `Usage <https://github.com/alammehio/rf-surveillance/blob/master/docs/source/contents/usage.rst>`_.


License
=======


* `GNU Affero General Public License v3.0`_


License
=======

* Free software: GNU Affero General Public License v3.0



.. LINKS

.. _GNU Affero General Public License v3.0: https://github.com/alammehio/rf-surveillance/blob/master/LICENSE

 

.. BADGE ALIASES

.. Build Status
.. Github Actions: Test Workflow Status for specific branch <branch>

.. |build| image:: https://img.shields.io/github/workflow/status/alammehio/rf-surveillance/Test%20Python%20Package/master?label=build&logo=github-actions&logoColor=%233392FF
    :alt: GitHub Workflow Status (branch)
    :target: https://github.com/alammehio/rf-surveillance/actions/workflows/test.yaml?query=branch%3Amaster


.. Documentation

.. |docs| image:: https://img.shields.io/readthedocs/rf-surveillance/latest?logo=readthedocs&logoColor=lightblue
    :alt: Read the Docs (version)
    :target: https://rf-surveillance.readthedocs.io/en/latest/

.. |pylint| image:: https://img.shields.io/badge/linting-pylint-yellowgreen
    :target: https://github.com/pylint-dev/pylint

.. PyPI

.. |release_version| image:: https://img.shields.io/pypi/v/rf-surveillance
    :alt: Production Version
    :target: https://pypi.org/project/rf-surveillance/

.. |wheel| image:: https://img.shields.io/pypi/wheel/rf-surveillance?color=green&label=wheel
    :alt: PyPI - Wheel
    :target: https://pypi.org/project/rf-surveillance

.. |supported_versions| image:: https://img.shields.io/pypi/pyversions/rf-surveillance?color=blue&label=python&logo=python&logoColor=%23ccccff
    :alt: Supported Python versions
    :target: https://pypi.org/project/rf-surveillance

.. Github Releases & Tags

.. |commits_since_specific_tag_on_main| image:: https://img.shields.io/github/commits-since/alammehio/rf-surveillance/v0.0.1/master?color=blue&logo=github
    :alt: GitHub commits since tagged version (branch)
    :target: https://github.com/alammehio/rf-surveillance/compare/v0.0.1..master

.. |commits_since_latest_github_release| image:: https://img.shields.io/github/commits-since/alammehio/rf-surveillance/latest?color=blue&logo=semver&sort=semver
    :alt: GitHub commits since latest release (by SemVer)

.. LICENSE (eg AGPL, MIT)
.. Github License

.. |gh-lic| image:: https://img.shields.io/badge/license-GNU_Affero-orange
    :alt: GitHub
    :target: https://github.com/alammehio/rf-surveillance/blob/master/LICENSE


.. Ruff linter for Fast Python Linting

.. |ruff| image:: https://img.shields.io/badge/codestyle-ruff-000000.svg
    :alt: Ruff
    :target: https://docs.astral.sh/ruff/


.. Local linux command: CTRL+Shift+Alt+R key 


.. Local Image as link

.. |dmc_image| image:: https://raw.githubusercontent.com/alammehio/rf-surveillance/master/media/xxxx.png
                :alt: DMC view which shows all the value. 2D view ; 3D view will contains 3 dimensions acceleration

.. |dmc_gif| image:: https://raw.githubusercontent.com/alammehio/rf-surveillance/master/media/xxx.gif
   :alt: Demo Preview
   :width: 600
