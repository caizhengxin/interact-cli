# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-27 23:56:55
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-28 00:17:51
from interact import interacts


config = {
    "name": {
        "type": "string",
        "default": "jankinca",
        "max_length": 10,
        "min_length": 1,
        "description": "Your name"
    }
}


if __name__ == "__main__":
    """
    Your name [jankinca]: sssssssssssss
    Error: Invalided `sssssssssssss`
    Your name [jankinca]: jankincai
    """

    print(interacts(config).name)
