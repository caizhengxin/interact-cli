# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-27 23:56:55
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-30 16:16:28
from interact import interacts


config = {
    "mac": {
        "type": "mac",
        "default": "aa:bb:cc:dd:ee:ff",
        "description": "MAC"
    },
    "ipv4": {
        "type": "ipv4",
        "default": "192.168.166.2",
        "description": "IPv4 address",
    },
    "ipv4_cidr": {
        "type": "cidr",
        "default": "192.168.166.2/24",
        "description": "IPv4 address",
    }
}


if __name__ == "__main__":
    """
    > MAC [aa:bb:cc:dd:ee:ff]: aa:bb:cc:dd:ee
    Error: Invalided `aa:bb:cc:dd:ee`
    """

    print(interacts(config).mac)
