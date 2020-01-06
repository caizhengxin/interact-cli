# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-23 22:45:03
# @Last Modified by:   JanKinCai
# @Last Modified time: 2020-01-06 22:50:25
import sys
# from typing import (
#     Optional, Tuple, Union, Any
# )

from interact.utils import CmdInputDict


class When(object):
    """When conditional expression

    :param wv(str): When value.
    :param cid(dict): Cmd input data.
    """

    def __init__(self, wv: str, cid: dict, *args, **kwargs) -> None:
        """init
        """

        self.wv = self.do_when_value(wv)
        self.cid = CmdInputDict(self.ext_cid(cid))

    def do_when_value(self, wv: str) -> str:
        """Deal when value.

        Args:
            param wv (str): When value.

        Returns:
            str: When value.
        """

        wv = wv.replace("false", "False").replace("true", "True")
        wv = wv.replace("&&", "and").replace("||", "or")

        return wv

    def ext_cid(self, cid: dict) -> dict:
        """Extension when

        Args:
            param cid (dict): Cmd input data.

        Returns:
            dict
        """

        ost = sys.platform

        cid["islinux"] = (ost == "linux")
        cid["iswin"] = (ost in ["win32", "cygwin"])
        cid["ismac"] = (ost == "darwin")

        return cid

    def do_when(self) -> bool:
        """
        Deal with when.

        Returns:
            bool: Expression result.
        """

        return eval(self.wv, self.cid)


def when(*args, **kwarags) -> bool:
    """Associate rules

    Returns:
        bool: Expression result.
    """

    return When(*args, **kwarags).do_when()
