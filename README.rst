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

.. code-block:: console

    Your Project name [interact-cli]:
    Project description [Interactive command line tool.]:
    Your name [jankincai]:
    Your email [jankincai12@gmail.com]:
    Project version [0.1.0]:
    Use code hosting platform [n]: y
    Select code hosting:
      1 - github
      2 - gitee
      3 - gitlab
    Choose from [1]:
    Your code hosting username [jankincai]:


* See demo_

Usage
-----

See interact.json_

interact:

.. code:: python

    from interact import interact


    if __name__ == "__main__":
        obj = interact("interact.json")
        print(obj)
        print(obj.version)

interacts:

.. code:: python

    from interact import interacts


    config = {
        "project_name": {
            "type": "string",
            "default": "interact-cli",
            "description": "Your Project name"
        },
        "description": {
            "type": "string",
            "default": "Interactive command line tool.",
            "description": "Project description"
        },
        "author": {
            "type": "string",
            "default": "jankincai",
            "description": "Your name"
        },
        "email": {
            "type": "string",
            "default": "jankincai12@gmail.com",
            "description": "Your email"
        },
        "version": {
            "type": "string",
            "default": "0.1.0",
            "description": "Project version"
        },
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
        obj = interacts(config)
        print(obj)
        print(obj.version)

load:

.. code:: python

    from interact import load


    if __name__ == "__main__":
        print(load("interact.json"))


loads:

.. code:: python

    from interact import loads


    if __name__ == "__main__":
        print(loads(config))

Credits
-------

This package was created with Cookiecutter_ and the `caizhengxin/cookiecutter-package`_ project template.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`caizhengxin/cookiecutter-package`: https://github.com/caizhengxin/cookiecutter-package
.. _demo: ./demo
.. _interact.json: ./demo/interact.json
