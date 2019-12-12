# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 21:03:34
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-12 21:28:53
from interact.base import Interact


config = {
    "iface": {
        "type": "string",
        "default": "enp1s0",
        "description": "Network card name"
    },
    "static": {
        "type": "boolean",
        "default": False,
        "description": "Static"
    },
    "a": {

    }
}


if __name__ == "__main__":
    interact = Interact(config)
    print(interact)
    print(interact.cli_items)
    print(interact.iface)
