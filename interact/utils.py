# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 10:46:50
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 10:47:08


class CmdInputDict(dict):
    """
    CmdInputDict
    """

    def __getattr__(self, name: str):
        """
        getattr
        """

        v = self[name]

        if isinstance(v, dict):
            return CmdInputDict(v)

        return v
