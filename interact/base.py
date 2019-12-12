# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 12:52:19
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-12 22:44:01
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

    def _parser(self, iconfig) -> dict:
        """
        Parser Interact cli config.
        """

        items = {}

        for k, v in self.iconfig.items():
            if not isinstance(v, dict):
                print("[+]: interact.json error.")
                sys.exit(1)

            prefix = v.get("description") or k
            default = v.get("default")
            if isinstance(default, bool):
                default = "y" if default else "n"

            input_info = f"{prefix} [{default}]:" if default is not None else f"{prefix}:"

            items[k] = conversion_type(types=v.get("type"), value=input(input_info) or default)

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
