# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 22:41:53
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-12 22:48:14
from __future__ import print_function
import json
import logging.config

from interact import settings
from interact.base import Interact


__version__ = "0.1.0"
__author__ = "jankincai"


logging.config.dictConfig(settings.LOGGING)


def load(iconfig:dict, *args, **kwargs) -> dict:
    """
    load

    :param iconfig: Interact cli config.

    :return: dict
    """

    return Interact(iconfig=iconfig, *args, **kwargs).get_interact_data()


def loads(file:str, *args, **kwargs) -> dict:
    """
    loads

    :param file: *.json file.

    :return: dict
    """

    with open(file) as f:
        iconfig = json.loads(f.read())

        return load(iconfig, *args, **kwargs)
