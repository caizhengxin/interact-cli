# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-26 23:15:03
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-30 16:04:17
from interact import interacts


config = {
    "port": {
        "type": "int",
        "default": 22,
        "max_value": 30,
        "min_value": 20,
        "description": "Port"
    }
}


if __name__ == "__main__":
    """
    Port [22]: 32
    Error: Invalided `32`, max_value=30, min_value=20
    Port [22]: 10
    Error: Invalided `10`, max_value=30, min_value=20
    Port [22]: 25
    """
    print(interacts(config).port)
