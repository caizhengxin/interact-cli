# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 12:52:19
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-15 22:59:22
from __future__ import print_function
import sys

from interact.types import conversion_type


class Interact(object):
    """
    Interact

    :param iconfig: Interact cli config.
    """

    def __init__(self, iconfig:dict, *args, **kwargs):
        """
        init
        """

        self.iconfig = iconfig
        self._cli_items = self.parser()

    def to_input(self, value:str, types:str, default:any, choice:list) -> any:
        """
        Interact input
        """

        v = conversion_type(types=types, value=input(value) or default)

        if isinstance(choice, list) and (v > len(choice) or v < 0):
            print("Error: Invalided choose")
            return self.to_input(value=value, types=types, default=default, choice=choice)

        return v


    def _parser_choice(self, choice:list, prefix:str) -> str:
        """
        Parsesr choice

        :param choice(list): choice
        :param prefix(str): description or key perfix

        :reeturn: str
        """

        prefix = f"Select {prefix}:"

        for i, chi in enumerate(choice, 1):
            prefix += f"\n  {i} - {chi}"

        prefix += f"\nChoose from"

        return prefix

    def _parser(self, iconfig) -> dict:
        """
        Parser Interact cli config.
        """

        items = {}

        for k, v in self.iconfig.items():

            prefix = v.get("description") or k
            default = v.get("default")
            choice = v.get("choice")
            types = v.get("type")

            if isinstance(default, bool):
                default = "y" if default else "n"

            if choice is not None:
                prefix = self._parser_choice(choice, prefix)
                default = default or 1

            input_info = f"{prefix} [{default}]:" if default is not None else f"{prefix}:"

            items[k] = self.to_input(value=input_info, types=types, default=default, choice=choice)

        return items

    def parser(self) -> dict:
        """
        Parser Interact cli config.
        """

        return self._parser(self.iconfig)

    def get_interact_data(self) -> dict:
        """
        Get interact data
        """

        return self._cli_items

    def __getattr__(self, attr):
        """
        getattr
        """

        try:
            return self.cli_items[attr]
        except Exception:
            pass
