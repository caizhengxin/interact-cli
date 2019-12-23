# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-23 22:45:03
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-23 23:33:47
import re


# (==|!=)$
reg = re.compile(r"^([a-zA-Z][0-9a-zA-Z_.]+) (==|!=) ([\S\s]+)$")


v = "ss_ss.zz == 'sss zz'"


def do_when(value):
    """"""

    v = reg.match(v)

    if v is None:
        return None

    attr = v.group(1)
    operator = v.group(2)
    v = v.group(3)

    if operator == "==":
        pass
