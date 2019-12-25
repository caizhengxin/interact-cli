# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 22:41:53
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 23:01:41
from __future__ import print_function
import json

from typing import (
    Any
)

from interact.base import Interact


__version__ = "0.2.0"
__author__ = "jankincai"


def interacts(iconfig: dict) -> Any:
    """
    Interacts

    :param iconfig(dict): Interact cli config.

    :return: any
    """

    return Interact(iconfig=iconfig)


def interact(file: str) -> Any:
    """
    interact

    :param file(str): xxxx.json file.

    :return: Any
    """

    with open(file) as f:
        return interacts(json.loads(f.read()))


def loads(iconfig: dict) -> dict:
    """
    loads

    :param iconfig(dict): Interact cli config.

    :return: dict
    """

    return interacts(iconfig=iconfig).get_interact_data()


def load(file: str) -> dict:
    """
    load

    :param file(str): xxxx.json file.

    :return: dict
    """

    with open(file) as f:
        return loads(json.loads(f.read()))
