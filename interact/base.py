# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 12:52:19
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 22:40:25
from __future__ import print_function
import sys
import json
import traceback

from typing import (
    Callable, Optional, Any, Dict
)

from interact.utils import CmdInputDict
from interact.when import when
from interact.fields import (
    StringField,
    BooleanField,
    IntField,
    ListField,
    ChoiceField,
)


class Interact(object):
    """
    Interact

    :param iconfig(dict): Interact cli config.
    """

    mapping_type_items: dict = {
        "string": StringField,
        "str": StringField,
        "boolean": BooleanField,
        "bool": BooleanField,
        "int": IntField,
        "list": ListField,
        "choice": ChoiceField,
    }

    def __init__(self, iconfig: dict, *args, **kwargs):
        """
        init
        """

        self.iconfig = iconfig
        self.cmd_input_items = self.parser()

    def get_mapping_type(self, name: str) -> Optional[Callable[[Any, str, Optional[list]], Any]]:
        """
        Get mapping type

        :param name(str): Type name.

        :return: callable
        """

        return self.mapping_type_items.get(name)

    def do_when(self, value: str) -> Any:
        """
        Deal with when
        """

        pass

    def _parser(self, iconfig) -> dict:
        """
        Parser Interact cli config.
        """

        items: Dict = {}

        for k, v in iconfig.items():

            description = v.get("description") or k
            default = v.get("default")
            choice = v.get("choice")
            types = v.get("type")
            whenstr = v.get("when")

            func: Any = self.get_mapping_type(types)

            if func is None:
                raise ValueError("Not support type.")

            if whenstr is not None and not when(whenstr, items):
                items[k] = None
                continue

            fobj = func(default=default, description=description, choice=choice)

            if not fobj.is_valid():
                raise ValueError(f"{description}, default value error.")

            items[k] = fobj.do()

        return items

    def parser(self) -> dict:
        """
        Parser Interact cli config.

        :return: dict
        """

        try:
            return self._parser(self.iconfig)
        except Exception as e:
            print("[-]:", e)
            traceback.print_exc()
            sys.exit(1)

    def get_interact_data(self) -> dict:
        """
        Get interact data
        """

        return self.cmd_input_items

    def __getattr__(self, name: str) -> Any:
        """
        getattr
        """

        try:
            return getattr(CmdInputDict(self.cmd_input_items), name)
        except KeyError:
            pass

    def __repr__(self) -> str:
        """
        repr
        """

        return json.dumps(self.cmd_input_items, indent=4)

    def __str__(self) -> str:
        """
        str
        """

        return self.__repr__()
