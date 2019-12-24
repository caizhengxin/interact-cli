# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-23 22:45:03
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 20:44:44
import re

from typing import (
    Optional, Tuple, Union, Any
)

from interact.utils import CmdInputDict


reg = re.compile(r"^([a-zA-Z_][0-9a-zA-Z_.]*) (==|!=) ([\S\s]+)$")


class When(object):
    """
    When rule

    :param wv(str): When value.
    :param cid(dict): Cmd input data.
    """

    mapping_boolean_true = [
        "y", "Y",
        "t", "T",
        "true", "True",
        True,
    ]

    mapping_boolean_false = [
        "n", "N",
        "f", "F",
        "false", "False",
        False,
    ]

    def __init__(self, wv: str, cid: dict, *args, **kwargs) -> None:
        """
        init
        """

        self.wv = wv
        self.cid = CmdInputDict(cid)
        self.attr = ""

    def get_cid_value(self, name: str) -> Union[str, int, float, bool, dict]:
        """
        Get cmd input data.

        :param name(str): Cmd input data(key)

        :return: Union[str, int, float, bool, dict]
        """

        nlist = name.split(".")
        cid = self.cid

        for n in nlist:
            cid = getattr(cid, n, None)

            if not isinstance(cid, CmdInputDict):
                break

        return cid

    def split_when(self) -> Optional[Tuple[str, str, str]]:
        """
        Split when value.

        :return: Optional[Tuple[str, str, str]]
        """

        v = reg.match(self.wv)

        if v is not None:
            return v.group(1), v.group(2), v.group(3)

        return v

    def do_when(self) -> bool:
        """
        Deal with when.
        """

        wvt = self.split_when()

        if wvt is None:
            return False

        self.attr, operator, value = wvt

        if operator == "==":
            return self == value
        elif operator == "!=":
            return self != value

        return False

    def get_other(self, other: Any) -> Tuple[Any, Any]:
        """
        To when value
        """

        v: Any = None

        cid = self.get_cid_value(self.attr or "")

        if other in self.mapping_boolean_false:
            v = False
        elif other in self.mapping_boolean_true:
            v = True
        elif isinstance(cid, str):
            v = cid.lstrip("'").rstrip("'").lstrip('"').rstrip('"')
        else:
            v = type(cid)(other)

        return cid, v

    def __eq__(self, other):
        """
        Operator ==
        """

        cid, other = self.get_other(other)

        return cid == other

    def __ne__(self, other):
        """
        Operator !=
        """

        cid, other = self.get_other(other)

        return cid != type(cid)(other)


def when(*args, **kwarags) -> bool:
    """
    Associate rules
    """

    try:
        return When(*args, **kwarags).do_when()
    except KeyError:
        raise ValueError("Key(when) value is wrong.")
