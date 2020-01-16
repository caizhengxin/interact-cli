# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 22:41:53
# @Last Modified by:   JanKinCai
# @Last Modified time: 2020-01-16 10:26:46
from __future__ import print_function
import sys
import json
# import traceback

from typing import (
    Any
)

from interact.base import Interact


__version__ = "0.5.0"
__author__ = "jankincai"


def interacts(iconfig: dict, *args, **kwargs) -> Any:
    """
    Interacts

    :param iconfig(dict): Interact cli config.

    :return: any
    """

    try:
        return Interact(iconfig=iconfig, *args, **kwargs)
    except Exception as e:
        # traceback.print_exc()
        print(f"[-]:", e)

    sys.exit(1)


def interact(file: str, *args, **kwargs) -> Any:
    """
    interact

    :param file(str): xxxx.json file.

    :return: Any
    """

    with open(file) as f:
        return interacts(json.loads(f.read()), *args, **kwargs)


def loads(iconfig: dict, *args, **kwargs) -> dict:
    """
    loads

    :param iconfig(dict): Interact cli config.

    :return: dict
    """

    return interacts(iconfig=iconfig, *args, **kwargs).get_interact_data()


def load(file: str, *args, **kwargs) -> dict:
    """
    load

    :param file(str): xxxx.json file.

    :return: dict
    """

    with open(file) as f:
        return loads(json.loads(f.read()), *args, **kwargs)
