# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2020-01-16 10:23:17
# @Last Modified by:   JanKinCai
# @Last Modified time: 2020-01-16 10:29:16
from interact import interacts
from interact import color


config = {
    "port": {
        "type": "int",
        "default": 22,
        "max_value": 30,
        "min_value": 20,
        "description": "Port"
    },
    "port2": {
        "type": "int",
        "default": 22,
        "max_value": 30,
        "min_value": 20,
        "color": color.COLOR_CYAN_BLUE,
        "description": "Port2"
    }
}


if __name__ == "__main__":
    print(interacts(config, color=color.COLOR_RED).port)
