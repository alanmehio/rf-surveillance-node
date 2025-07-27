RF Surveillance Node
====================

| Radio Frequency Surveillance Node. This is one of four applications


------

.. start-badges see https://shields.io/badges and collection see https://github.com/inttter/md-badges

| |build| |release_version| |wheel|
| |docs| |pylint| |supported_versions|
| |ruff| |gh-lic| |commits_since_specific_tag_on_main|



Different nodes sends signal based on pre-configured required power strength. Each node
can have unlimited antenna scanners; each antenna is given a range of frequency slice to scan and report
the power which exceed the given threshold which is defined in the setting file
The antenna sends the signal data into a transmitter device found in the node.
The data sent is: central frequency in MHz , the power in dBm, IQ sample (imaginary number) where the sample size is configured to 1024 numbers.
The sample size can be in hundred thousands. The sample rate is 1.24 millions samples per second; it can be configured to tens of millions per second.
The node works in a plug and play which means high quality SDR devices (RTL-SDR, USRP, BladeRF, HackRF etc..) can be attached to sample on much higher rate.

|rf_node|
|rf_node_console|




Change Log
==========
 `Change Log <https://github.com/alanmehio/rf-surveillance-node/blob/main/CHANGELOG.rst>`_.

Quickstart
==========
| `Usage <https://github.com/alanmehio/rf-surveillance-node/blob/main/docs/source/contents/usage.rst>`_.


License
=======


* `GNU Affero General Public License v3.0`_


License
=======

* Free software: GNU Affero General Public License v3.0



.. LINKS

.. _GNU Affero General Public License v3.0: https://github.com/alanmehio/rf-surveillance-node/blob/main/LICENSE



.. BADGE ALIASES

.. Build Status
.. Github Actions: Test Workflow Status for specific branch <branch>

.. |build| image:: https://img.shields.io/github/workflow/status/alanmehio/rf-surveillance-node/Test%20Python%20Package/main?label=build&logo=github-actions&logoColor=%233392FF
    :alt: GitHub Workflow Status (branch)
    :target: https://github.com/alanmehio/rf-surveillance-node/actions/workflows/test.yaml?query=branch%3Amain


.. Documentation

.. |docs| image:: https://img.shields.io/readthedocs/rf-surveillance-node/latest?logo=readthedocs&logoColor=lightblue
    :alt: Read the Docs (version)
    :target: https://rf-surveillance-node.readthedocs.io/en/latest/

.. |pylint| image:: https://img.shields.io/badge/linting-pylint-yellowgreen
    :target: https://github.com/pylint-dev/pylint

.. PyPI

.. |release_version| image:: https://img.shields.io/pypi/v/rf-surveillance-node
    :alt: Production Version
    :target: https://pypi.org/project/rf-surveillance-node/

.. |wheel| image:: https://img.shields.io/pypi/wheel/rf-surveillance-node?color=green&label=wheel
    :alt: PyPI - Wheel
    :target: https://pypi.org/project/rf-surveillance-node

.. |supported_versions| image:: https://img.shields.io/pypi/pyversions/rf-surveillance-node?color=blue&label=python&logo=python&logoColor=%23ccccff
    :alt: Supported Python versions
    :target: https://pypi.org/project/rf-surveillance-node

.. Github Releases & Tags

.. |commits_since_specific_tag_on_main| image:: https://img.shields.io/github/commits-since/alanmehio/rf-surveillance-node/v0.0.1/main?color=blue&logo=github
    :alt: GitHub commits since tagged version (branch)
    :target: https://github.com/alanmehio/rf-surveillance-node/compare/v0.0.1..main

.. |commits_since_latest_github_release| image:: https://img.shields.io/github/commits-since/alanmehio/rf-surveillance-node/latest?color=blue&logo=semver&sort=semver
    :alt: GitHub commits since latest release (by SemVer)

.. LICENSE (eg AGPL, MIT)
.. Github License

.. |gh-lic| image:: https://img.shields.io/badge/license-GNU_Affero-orange
    :alt: GitHub
    :target: https://github.com/alanmehio/rf-surveillance-node/blob/main/LICENSE


.. Ruff linter for Fast Python Linting

.. |ruff| image:: https://img.shields.io/badge/codestyle-ruff-000000.svg
    :alt: Ruff
    :target: https://docs.astral.sh/ruff/


.. Local linux command: CTRL+Shift+Alt+R key


.. Local Image as link


.. |rf_node| image:: https://github.com/alanmehio/rf-surveillance-node/blob/main/media/rf-node.png
                :alt: RF Surveillance Node

.. |rf_node_console| image:: https://github.com/alanmehio/rf-surveillance-node/blob/main/media/screen/rf-node-console.gif
                :alt: RF Surveillance Node Console Display for two RTL-SDR devices

.. |rf_central| image:: https://github.com/alanmehio/rf-surveillance-node/blob/main/media/rf-central.jpeg
                :alt: RF Surveillance Central(Server)
.. |rf_central_console| image:: https://github.com/alanmehio/rf-surveillance-node-node/blob/main/media/screen/rf-central-console.gif
                :alt: RF Surveillance Central(Server) console output


