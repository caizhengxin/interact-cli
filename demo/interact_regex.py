# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-26 23:15:03
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-27 21:37:07
from interact import load


"""
IPv4 address [192.168.166.12]: 22
Error: Invalided `22`
IPv4 address [192.168.166.12]: 192.168.166.2
{'ipv4': '192.168.166.2'}
"""


if __name__ == "__main__":
    print(load("network.json"))
