# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-23 12:37:34
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-25 16:54:58
# import sys

from typing import (
    Any, Optional, List, Union
)


class BaseField(object):
    """
    BaseField

    :param default(any): input default, default ``None``
    :param description(str): prefix description, default ``""``
    """

    message = "Invalided `{value}`"
    valid_type: Any = None

    def __init__(self, default: Any=None, description: str="", *args, **kwargs):
        """
        init
        """

        self.default = default
        self.descripiton = description
        self.is_valid()

    def is_valid(self) -> bool:
        """
        Valid default

        :return: bool
        """

        assert self.valid_type is not None, "valid_type cannot be None."

        if not isinstance(self.default, self.valid_type):
            return False

        return True

    def print_message(self, **kwargs) -> None:
        """
        print message

        :return: None
        """

        print(f"Error: {self.message.format(**kwargs)}")

    def to_default(self, v: Any) -> Any:
        """
        To default

        :param v(any): default
        """

        return v

    def do_default(self) -> str:
        """
        Deal with default

        :return: str
        """

        default = self.default

        if isinstance(default, list):
            default = ", ".join(default)

        return f"[{self.to_default(default)}]" if default is not None else ""

    def do(self) -> Any:
        """
        Deal with

        :return: any
        """

        v = self.to_input() or self.default

        # Reason isinstance(v, int)  v(bool) --> True
        if not isinstance(v, str) and not (isinstance(v, int) and not isinstance(v, bool)):
            return v

        try:
            return self.to_value(v)
        except Exception as e:
            # print("[+]:", e)
            self.print_message(value=v)

        return self.do()

    def to_value(self, v: Any) -> Any:
        """
        To value

        :param v(str): cmd data

        :return: any
        """

        pass

    def pre_input(self) -> str:
        """
        Pre input

        :return: str
        """

        return ""

    def post_input(self) -> str:
        """
        Post input

        :return: str
        """

        return ""

    def to_input(self) -> str:
        """
        To input

        :return: str
        """

        v = f"{self.pre_input()}{self.descripiton} {self.do_default()}{self.post_input()}: "

        return input(v)


class BooleanField(BaseField):
    """
    BoleanField
    """

    mapping_boolean_true = [
        "y", "Y",
        "t", "T",
        "true", "True",
        True,
    ]

    mapping_boolean_false = [
        "n", "N",
        "f", "F",
        "false", "False",
        False,
    ]

    valid_type = bool

    def to_default(self, v: bool) -> Any:
        """
        To default

        :param v(bool): Default to input string

        :return: any
        """

        return "y" if v else "n"

    def to_value(self, v: str) -> bool:
        """
        To value

        :param v(str): cmd data

        :return: bool
        """

        if v in self.mapping_boolean_true:
            return True

        if v in self.mapping_boolean_false:
            return False

        raise ValueError()


class StringField(BaseField):
    """
    StringField
    """

    valid_type = str

    def to_value(self, v: str) -> str:
        """
        To value

        :param v(str): cmd data

        :return: str
        """

        return str(v)


class IntField(BaseField):
    """
    IntField
    """

    valid_type = int

    def to_value(self, v: str) -> int:
        """
        To value

        :param v(str): cmd data

        :return: int
        """

        return int(v)


class FloatField(BaseField):
    """
    FloatField
    """

    valid_type = float

    def to_value(self, v: str) -> float:
        """
        To value

        :param v(str): cmd data

        :return: float
        """

        return float(v)


class ListField(BaseField):
    """
    ListField
    """

    valid_type = list

    def to_value(self, v: Any) -> list:
        """
        To value

        :param v(any): cmd data

        :return: list
        """

        if isinstance(v, list):
            return v

        return v.replace(", ", ",").split(",")


class ChoiceField(BaseField):
    """
    ChoiceField

    :param choice(list): choice, default ``[]``
    :param default(any): input default, default ``None``
    :param description(str): prefix description, default ``""``
    """

    valid_type = int

    def __init__(self, choice: list=[], default: Any=None, description: str="", *args, **kwargs):
        """
        init
        """

        self.choice = choice
        super(ChoiceField, self).__init__(default=default or 1, description=description, *args, **kwargs)

    def to_value(self, v: Any) -> Any:
        """
        To value

        :param v(any): cmd data

        :return: any
        """

        return self.choice[int(v) - 1]

    def pre_input(self) -> str:
        """
        Pre input

        :return: str
        """

        input_list = [
            f"Select {self.descripiton.lower()}:",
        ]

        choice_list = [f"  {i} - {chi}" for i, chi in enumerate(self.choice, 1)]
        choice_list.append(f"Choose from")
        input_list.extend(choice_list)

        return "\n".join(input_list)

    def to_input(self) -> str:
        """
        To input

        :return: str
        """

        v = f"{self.pre_input()} {self.do_default()}{self.post_input()}: "

        return input(v)
