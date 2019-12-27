# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-26 23:15:03
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-28 00:02:51
from interact import interacts


config = {
    "ipv4": {
        "type": "string",
        "regex": r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$",
        "default": "192.168.166.12",
        "description": "IPv4 address"
    }
}


if __name__ == "__main__":
    """
    IPv4 address [192.168.166.12]: 22
    Error: Invalided `22`
    IPv4 address [192.168.166.12]: 192.168.166.2
    """

    print(interacts(config).ipv4)
