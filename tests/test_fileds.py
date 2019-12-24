# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 20:52:19
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 20:52:51
from interact.fields import (
    IntField,
    ChoiceField,
    ListField,
    BooleanField,
)


if __name__ == "__main__":
    print(IntField(1, "cx").do())
    print(IntField(description="cx").do())
    print(ChoiceField(["A", "B"], description="DS").do())
    print(ListField(default=["192.168.166.120/24", "192.168.166.120/24"], description="IPv4").do())
    obj = BooleanField(True, description="u_cython")
    print(obj.is_valid())
    print(obj.do())
