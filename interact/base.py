# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 12:52:19
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-30 16:13:27
from __future__ import print_function
# import sys
import json
# import traceback

from typing import (
    Callable, Optional, Any, Dict
)

from interact.error import ConfigError
from interact.utils import CmdInputDict
from interact.when import when
from interact.fields import (
    StringField,
    BooleanField,
    IntField,
    ListField,
    ChoiceField,
    FloatField,
    MACField,
    IPv4Field,
    HexField,
    CIDRField,
)


class Interact(object):
    """
    Interactive command line

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
        "float": FloatField,
        "double": FloatField,
        "mac": MACField,
        "ipv4": IPv4Field,
        "cidr": CIDRField,
        "hex": HexField,
    }

    def __init__(self, iconfig: dict, prefix=">", *args, **kwargs):
        """
        init
        """

        self.iconfig = iconfig
        self.prefix = prefix
        self.cmd_input_items = self.parser()

    def get_mapping_type(self, name: str) -> Optional[Callable[[Any, str, Optional[list]], Any]]:
        """
        Get mapping type

        :param name(str): Type name.

        :return: callable
        """

        return self.mapping_type_items.get(name) or self.mapping_type_items.get(name.lower())

    def is_iconfig_valid(self) -> None:
        """
        Check iconfig
        """

        for k, v in self.iconfig.items():
            if not isinstance(v, dict):
                raise ConfigError(f"{k}: value must be dict type.")

            types = v.get("type")

            if types is None or types not in self.mapping_type_items.keys():
                raise ConfigError(f"{k}: type is not supported.")

            fobj = self.get_mapping_type(types)(**v)

            if not fobj.is_default_valid():
                raise ConfigError(f"{k}: default value error.")

    def _parser(self, iconfig) -> dict:
        """
        Parser Interact cli config.
        """

        items: Dict = {}

        for k, v in iconfig.items():

            v["description"] = v.get("description") or k

            whenstr = v.get("when")

            if whenstr is not None and not when(whenstr, items):
                items[k] = None
                continue

            items[k] = self.get_mapping_type(v["type"])(prefix=self.prefix, **v).do()

        return items

    def parser(self) -> dict:
        """
        Parser Interact cli config.

        :return: dict
        """

        self.is_iconfig_valid()
        return self._parser(self.iconfig)

    def get_interact_data(self) -> dict:
        """
        Get interact data
        """

        return self.cmd_input_items

    def register(self, name: str, field: object) -> None:
        """
        Registered custom field.

        :param name(str): Type name.
        :param field(object): Field object.

        :return: None
        """

        self.mapping_type_items[name] = field

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
