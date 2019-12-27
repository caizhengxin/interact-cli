# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-28 00:06:56
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-28 00:14:06
from interact import interacts


config = {
    "use_code_hosting": {
        "type": "boolean",
        "default": True,
        "description": "Use code hosting platform"
    },
    "code_hosting": {
        "type": "choice",
        "default": 1,
        "choice": [
            "github",
            "gitee",
            "gitlab"
        ],
        "description": "Code hosting",
        "when": "use_code_hosting == true"
    },
    "code_hosting_username": {
        "type": "string",
        "default": "jankincai",
        "description": "Your code hosting username",
        "when": "use_code_hosting == true"
    }
}


if __name__ == "__main__":
    """
    Use code hosting platform [y]: y
    Select code hosting:
    1 - github
    2 - gitee
    3 - gitlab
    Choose from [1]:
    Your code hosting username [jankincai]: jankincai

    {'use_code_hosting': True, 'code_hosting': 'github', 'code_hosting_username': 'jankincai'}
    """

    """
    Use code hosting platform [y]: n
    {'use_code_hosting': False, 'code_hosting': None, 'code_hosting_username': None}
    """

    print(interacts(config).get_interact_data())
