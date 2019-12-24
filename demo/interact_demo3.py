# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 22:32:12
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 22:43:14
from interact import interacts


if __name__ == "__main__":
    obj = interacts("interact.json")
    print(obj)
    print(obj.version)
