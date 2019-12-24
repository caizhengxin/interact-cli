# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 21:12:56
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 23:06:45
from interact import loads


config = {
    "project_name": {
        "type": "string",
        "default": "interact-cli",
        "description": "Your Project name"
    },
    "description": {
        "type": "string",
        "default": "Interactive command line tool.",
        "description": "Project description"
    },
    "author": {
        "type": "string",
        "default": "jankincai",
        "description": "Your name"
    },
    "email": {
        "type": "string",
        "default": "jankincai12@gmail.com",
        "description": "Your email"
    },
    "version": {
        "type": "string",
        "default": "0.1.0",
        "description": "Project version"
    },
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
    print(loads(config))
