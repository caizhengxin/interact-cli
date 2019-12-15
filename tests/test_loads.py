# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 22:49:39
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-13 12:41:24
import os

from interact import loads


base_dir = os.path.dirname(os.path.abspath(__file__))
json_file = os.path.join(base_dir, "interact.json")


if __name__ == "__main__":
    print(loads(json_file))
