# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 12:52:19
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-23 23:32:21
from __future__ import print_function
import sys

from interact.fields import (
    StringField,
    BooleanField,
    IntField,
    ListField,
    ChoiceField,
)


class CmdInputDict(dict):
    """
    CmdInputDict
    """

    def __getattr__(self, name:str):
        """
        getattr
        """

        v = self[name]

        if isinstance(v, dict):
            return CmdInputDict(v)

        return v


class Interact(object):
    """
    Interact

    :param iconfig: Interact cli config.
    """

    mapping_type_items = {
        "string": StringField,
        "str": StringField,
        "boolean": BooleanField,
        "bool": BooleanField,
        "int": IntField,
        "list": ListField,
        "choice": ChoiceField,
    }

    def __init__(self, iconfig:dict, *args, **kwargs):
        """
        init
        """

        self.iconfig = iconfig
        self.cmd_input_items = self.parser()

    def get_mapping_type(self, name:str) -> object:
        """
        Get mapping type

        :param name(str): Type name.

        :return: object
        """

        return self.mapping_type_items.get(name)

    def do_when(self, value:str) -> any:
        """
        Deal with when
        """

        pass

    def _parser(self, iconfig) -> dict:
        """
        Parser Interact cli config.
        """

        items = {}

        for k, v in self.iconfig.items():

            description = v.get("description") or k
            default = v.get("default")
            choice = v.get("choice")
            types = v.get("type")
            when = v.get("when")

            fobj = self.get_mapping_type(types)(default=default, description=description, choice=choice)

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
            sys.exit(1)

    def get_interact_data(self) -> dict:
        """
        Get interact data
        """

        return self.cmd_input_items

    def __getattr__(self, name:str):
        """
        getattr
        """

        try:
            return getattr(CmdInputDict(self.cmd_input_items), name)
        except KeyError:
            pass
