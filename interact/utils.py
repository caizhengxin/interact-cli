# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 10:46:50
# @Last Modified by:   JanKinCai
# @Last Modified time: 2020-01-06 22:16:54


class CmdInputDict(dict):
    """CmdInputDict
    """

    def __init__(self, interable: dict, *args, **kwargs):
        """init
        """

        interable.update(self.do_interable(interable))
        super().__init__(interable)

    def do_interable(self, interable: dict) -> dict:
        """Deal args
        """

        items = {}

        for k, v in interable.items():
            if isinstance(v, dict):
                items.update(self.do_interable(v))
            else:
                items[v] = v

        return items

    def __getitem__(self, name: str) -> any:
        """getitem
        """

        v = self.get(name)

        if isinstance(v, dict):
            return self.__class__(v)

        return v

    def __getattr__(self, name: str) -> any:
        """getattr
        """

        return self.__getitem__(name)
