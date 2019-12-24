# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 22:32:12
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 23:02:12
from interact import interact


if __name__ == "__main__":
    obj = interact("interact.json")
    print(obj)
    print(obj.version)
