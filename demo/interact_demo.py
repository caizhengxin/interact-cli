# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 21:12:56
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-27 23:55:04
from interact import load


"""
Your Project name [interact-cli]:
Project description [Interactive command line tool.]:
Your name [jankincai]:
Your email [jankincai12@gmail.com]:
Project version [0.1.0]:
Use code hosting platform [n]: y
Select code hosting:
    1 - github
    2 - gitee
    3 - gitlab
Choose from [1]:
Your code hosting username [jankincai]:
"""


if __name__ == "__main__":
    print(load("interact.json"))
