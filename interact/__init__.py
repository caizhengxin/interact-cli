# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 22:41:53
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 22:29:33
from __future__ import print_function
import json

from typing import (
    Any
)

from interact.base import Interact


__version__ = "0.1.0"
__author__ = "jankincai"


def interact(iconfig: dict) -> Any:
    """
    Interact

    :param iconfig(dict): Interact cli config.

    :return: any
    """

    return Interact(iconfig=iconfig)


def interacts(file: str) -> Any:
    """
    interacts

    :param file(str): xxxx.json file.

    :return: Any
    """

    with open(file) as f:
        return interact(json.loads(f.read()))


def load(iconfig: dict) -> dict:
    """
    load

    :param iconfig(dict): Interact cli config.

    :return: dict
    """

    return interact(iconfig=iconfig).get_interact_data()


def loads(file: str) -> dict:
    """
    loads

    :param file(str): xxxx.json file.

    :return: dict
    """

    with open(file) as f:
        return load(json.loads(f.read()))
