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
* mac
* ipv4
* cidr, eg: ``192.168.1.1/24``
* hex

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

.. code:: python

    from interact import interacts


    config = {
        "ipv4": {
            "type": "string",
            "regex": r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$",
            "default": "192.168.166.12",
            "description": "IPv4 address"
        }
    }


    if __name__ == "__main__":
        """
        IPv4 address [192.168.166.12]: 22
        Error: Invalided `22`
        IPv4 address [192.168.166.12]: 192.168.166.2
        """

        print(interacts(config).ipv4)

when:

.. code:: python

    from interact import interacts


    config = {
        "use_code_hosting": {
            "type": "boolean",
            "default": True,
            "description": "Use code hosting platform"
        },
        "code_hosting": {
            "type": "choice",
            "default": 1,
            "choice": [
                "github",
                "gitee",
                "gitlab"
            ],
            "description": "Code hosting",
            "when": "use_code_hosting == true"
        },
        "code_hosting_username": {
            "type": "string",
            "default": "jankincai",
            "description": "Your code hosting username",
            "when": "use_code_hosting == true"
        }
    }


    if __name__ == "__main__":
        """
        Use code hosting platform [y]: y
        Select code hosting:
        1 - github
        2 - gitee
        3 - gitlab
        Choose from [1]:
        Your code hosting username [jankincai]: jankincai

        {'use_code_hosting': True, 'code_hosting': 'github', 'code_hosting_username': 'jankincai'}
        """

        """
        Use code hosting platform [y]: n
        {'use_code_hosting': False, 'code_hosting': None, 'code_hosting_username': None}
        """

        print(interacts(config).get_interact_data())

See demo_

Credits
-------

This package was created with Cookiecutter_ and the `caizhengxin/cookiecutter-package`_ project template.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`caizhengxin/cookiecutter-package`: https://github.com/caizhengxin/cookiecutter-package
.. _demo: ./demo
.. _interact.json: ./demo/interact.json
.. _network.json: ./demo/network.json
