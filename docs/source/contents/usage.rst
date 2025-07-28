Usage
=====

------------
Installation
------------

| **rfnode** is available on PyPI hence you can use `pip` to install it.

It is recommended to perform the installation in an isolated `python virtual environment` (env).
You can create and activate an `env` using any tool of your preference (ie `virtualenv`, `venv`, `pyenv`).

Assuming you have 'activated' a `python virtual environment`:

.. code-block:: shell

  python -m pip install rfnode


---------------
Simple Use Case
---------------

| Common Use Case for the rfnode 

.. code-block:: shell

  rfnode  setting.json -vvv -ld /home/alan/tmp
  **setting.json**  the setting file for frequency range and power threshold 
| **vvv**: extra verbose 
| **ld**: log file directory location
|
| Common Use Case for the dmcview in simulation mode


--------------
Running PyTest 
--------------
| PyTest can be run from command line.

.. code-block:: shell
  
  python -m pip install -e . rfnode[test]
  pytest



