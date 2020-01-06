# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-23 22:45:03
# @Last Modified by:   JanKinCai
# @Last Modified time: 2020-01-06 22:17:44
# from typing import (
#     Optional, Tuple, Union, Any
# )

from interact.utils import CmdInputDict


class When(object):
    """
    When rule

    :param wv(str): When value.
    :param cid(dict): Cmd input data.
    """

    def __init__(self, wv: str, cid: dict, *args, **kwargs) -> None:
        """
        init
        """

        self.wv = self.do_when_value(wv)
        self.cid = CmdInputDict(cid)

    def do_when_value(self, wv: str) -> str:
        """Deal when value.

        Args:
            param wv (str): When value.

        Returns:
            str: When value.
        """

        return wv.replace("false", "False").replace("true", "True")

    def do_when(self) -> bool:
        """
        Deal with when.
        """

        return eval(self.wv, self.cid)


def when(*args, **kwarags) -> bool:
    """
    Associate rules
    """

    return When(*args, **kwarags).do_when()
