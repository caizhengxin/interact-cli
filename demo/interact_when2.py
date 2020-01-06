# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-28 00:06:56
# @Last Modified by:   JanKinCai
# @Last Modified time: 2020-01-06 22:50:56
from interact import loads


config = {
    "test1": {
        "type": "boolean",
        "default": True,
        "description": "Test1"
    },
    "test2": {
        "type": "boolean",
        "default": True,
        "description": "Test2"
    },
    "test3": {
        "type": "boolean",
        "default": True,
        "description": "Test3",
        "when": "test1 == true && test2 == true" # && or and
    },
    "test4": {
        "type": "boolean",
        "default": True,
        "description": "Test4",
        "when": "islinux",
    },
}


if __name__ == "__main__":
    print(loads(config))
