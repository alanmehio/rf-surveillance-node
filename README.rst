RF Surveillance

| Radio Frequency Surveillance is a three  separated applications


------

.. start-badges see https://shields.io/badges and collection see https://github.com/inttter/md-badges

| |build| |release_version| |wheel|
| |docs| |pylint| |supported_versions|
| |ruff| |gh-lic| |commits_since_specific_tag_on_main|


RF-Node
=======
Different nodes sends signal based on pre-configured required power strength. Each node
can have unlimited antenna scanners; each antenna is given a range of frequency slice to scan and report
the power which exceed the given threshold which is defined in the setting file
The antenna sends the signal data into a transmitter device found in the node.
The data sent is: central frequency in MHz , the power in dBm, IQ sample (imaginary number) where the sample size is configured to 1024 numbers

|rf_node|


RF-Central
==========
|rf_central|

Receive signal strength from different nodes.
Process them and extract different meta data#
Display the high power signal on the console and give a warning (beep) in case
any frequency exceed the desired power defined when the RF Central application starts ( command line input)
This application contains a calculation engine based on Machine Learning Model to find different useful information
about the samples high power signal frequency.

RF Sink
=======
This application is a GUI application (Desktop) which query the RF central(sever) to extract the
already calculated meta data with different search criteria
|rf_sink1|
|rf_sink2|
|rf_sink3|

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


.. |rf_node| image:: https://github.com/alanmehio/rf-surveillance/blob/v1/media/rf-node.png
                :alt: RF Surveillance Node

.. |rf_central| image:: https://github.com/alanmehio/rf-surveillance/blob/v1/media/rf-central.jpeg
                :alt: RF Surveillance Central(Server)

.. |rf_sink1| image:: https://github.com/alanmehio/rf-surveillance/blob/v1/media/rf-sink1.jpeg
                :alt: RF Surveillance Sink(Client)

.. |rf_sink2| image:: https://github.com/alanmehio/rf-surveillance/blob/v1/media/rf-sink2.jpeg
                :alt: RF Surveillance Sink(Client)

.. |rf_sink3| image:: https://github.com/alanmehio/rf-surveillance/blob/v1/media/rf-sink3.jpeg
                :alt: RF Surveillance Sink(Client)


