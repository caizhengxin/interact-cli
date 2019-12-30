# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-23 12:37:34
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-30 16:12:52
# import sys
import re
from typing import (
    Any,
)


class BaseField(object):
    """
    BaseField

    :param default(any): Input default, default ``None``
    :param description(str): Prefix description, default ``""``
    """

    message = "Invalided `{value}`"
    valid_type: Any = None

    def __init__(self, default: Any = None, description: str = "", prefix=">", *args, **kwargs):
        """
        init
        """

        self.default = default
        self.prefix = prefix
        self.descripiton = description

    def is_default_valid(self) -> bool:
        """
        Verification default is valid.

        :return: bool
        """

        assert self.valid_type is not None, "valid_type cannot be None."

        if not self.default:
            return True

        if not isinstance(self.default, self.valid_type):
            return False

        if not self.is_valid(self.default):
            return False

        return True

    def is_valid(self, iv: str) -> bool:
        """
        Verification input value is valid.

        :param iv(str): Input value.

        :return: bool
        """

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
            v = self.to_value(v)

            if not self.is_valid(v):
                raise ValueError()

            return v
        except Exception:
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
        v = f"{self.prefix} {v}" if self.prefix else v

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
    regex = None

    def __init__(self, default: Any = None, description: str = "", min_length: int = None,
                 max_length: int = None, regex: str = "", *args, **kwargs):
        """
        init
        """

        regex = self.regex or regex or ""
        self.regex = re.compile(regex) if regex else regex
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(default=default, description=description, *args, **kwargs)


    def is_valid(self, iv: str) -> bool:
        """
        Verification input value is valid.

        :param iv(str): Input value.

        :return: bool
        """

        if (self.max_length is None or len(iv) < self.max_length) \
           and (self.min_length is None or len(iv) >= self.min_length) \
           and (not self.regex or self.regex.match(iv) is not None):
            return True

        return False

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

    def __init__(self, default: Any = None, description: str = "",
                 max_value: int = None, min_value: int = None, *args, **kwargs):
        """
        init
        """

        super().__init__(default=default, description=description, *args, **kwargs)
        self.max_value = max_value
        self.min_value = min_value

    def is_valid(self, iv: str) -> bool:
        """
        Verification input value is valid.

        :param iv(str): Input value.

        :return: bool
        """

        if (self.max_value is None or iv < self.max_value) and (self.min_value is None or iv >= self.min_value):
            return True

        return False

    def print_message(self, **kwargs) -> None:
        """
        print message

        :return: None
        """

        msg = f"Error: {self.message.format(**kwargs)}"

        if self.max_value is not None:
            msg += f", max_value={self.max_value}"

        if self.min_value is not None:
            msg += f", min_value={self.min_value}"

        print(msg)

    def to_value(self, v: str) -> int:
        """
        To value

        :param v(str): cmd data

        :return: int
        """

        return int(v)


class FloatField(IntField):
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


class ListField(StringField):
    """
    ListField
    """

    valid_type = list

    def is_valid(self, iv: list) -> bool:
        """
        Verification input value is valid.

        :param iv(list): Input value.

        :return: bool
        """

        for v in iv:
            if super().is_valid(v) is False:
                return False

        return True

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

    def __init__(self, choice: list = [], default: Any = None, description: str = "", *args, **kwargs):
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

        prefix = "Choose from"
        prefix = f"{self.prefix} {prefix}" if self.prefix else prefix
        choice_list.append(prefix)
        input_list.extend(choice_list)

        return "\n".join(input_list)

    def to_input(self) -> str:
        """
        To input

        :return: str
        """

        v = f"{self.pre_input()} {self.do_default()}{self.post_input()}: "
        v = f"{self.prefix} {v}" if self.prefix else v

        return input(v)


class MACField(StringField):
    """
    MACField
    """

    regex = r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"


class IPv4Field(StringField):
    """
    IPv4Field
    """

    regex = r"^(\d{1,3}.){3}\d{1,3}$"


class CIDRField(StringField):
    """
    CIDRField

    Example::

        192.168.1.1/24
    """

    regex = r"^(\d{1,3}.){3}\d{1,3}/\d{1,2}$"


class HexField(StringField):
    """
    HexField
    """

    regex = r"^([0-9a-fA-F]{2})*$"
