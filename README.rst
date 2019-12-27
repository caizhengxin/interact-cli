============
Interact cli
============

.. image:: https://img.shields.io/pypi/v/interact-cli.svg?branch=master&color=blue
        :target: https://pypi.python.org/pypi/interact-cli
        :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/interact-cli.svg?branch=master&color=blue
        :target: https://pypi.python.org/pypi/interact-cli

.. image:: https://img.shields.io/pypi/dm/interact-cli.svg?branch=master&color=blue
        :target: https://pypi.python.org/pypi/interact-cli

.. image:: https://api.travis-ci.com/caizhengxin/interact-cli.svg?branch=master&color=blue
        :target: https://travis-ci.org/caizhengxin/interact-cli/?branch=master

.. image:: https://readthedocs.org/projects/interact-cli/badge/?version=latest
        :target: https://interact-cli.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/github/languages/code-size/caizhengxin/interact-cli.svg?branch=master
        :target: https://github.com/caizhengxin/interact-cli

.. image:: https://img.shields.io/pypi/l/interact-cli.svg
        :target: https://github.com/caizhengxin/interact-cli/blob/master/LICENSE

Interactive command line tool.

* Github repo: https://github.com/caizhengxin/interact-cli
* Documentation: https://interact-cli.readthedocs.io
* Free software: BSD

Features
--------

* Interact input
* Supports multiple data types
* Support input check
* Support regex, see network.json_

Support type
------------

* boolean
* string
* int
* float
* list
* choice

Installation
------------

To install interact-cli, run this command in your terminal:

.. code-block:: console

    $ pip3 install interact-cli

or:

.. code-block:: console

    $ git clone https://github.com/caizhengxin/interact-cli.git
    $ cd interact-cli
    $ pip3 install -e .

Demo
----

* See demo_

Usage
-----

See interact.json_

string:

.. code:: python

    from interact import interacts


    config = {
        "name": {
            "type": "string",
            "default": "jankinca",
            "max_length": 10,
            "min_length": 1,
            "description": "Your name"
        }
    }


    if __name__ == "__main__":
        """
        Your name [jankinca]: sssssssssssss
        Error: Invalided `sssssssssssss`
        Your name [jankinca]: jankincai
        """
        print(interacts(config).name)

regex:

.. include:: ./demo/interact_regex.py

Credits
-------

This package was created with Cookiecutter_ and the `caizhengxin/cookiecutter-package`_ project template.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`caizhengxin/cookiecutter-package`: https://github.com/caizhengxin/cookiecutter-package
.. _demo: ./demo
.. _interact.json: ./demo/interact.json
.. _network.json: ./demo/network.json
