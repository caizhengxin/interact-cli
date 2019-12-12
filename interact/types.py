# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 21:32:30
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-12 23:07:25
"""
- string/str
- boolean/bool
- int
- float
- dict
- list
"""


def to_int(value:str) -> int:
    """
    Conversion int type
    """

    return int(value)


def to_boolean(value:str) -> bool:
    """
    Conversion boolean type
    """

    return True if value.lower() == "y" else False


def to_string(value:str) -> str:
    """
    Conversion string type
    """

    return value


def to_float(value:str) -> float:
    """
    Conversion float type
    """

    return float(value)


def to_list(value:str) -> list:
    """
    Conversion list type
    """

    return value.split(",")


data_type_mapping = {
    "int": to_int,
    "bool": to_boolean,
    "boolean": to_boolean,
    "float": to_float,
}


def conversion_type(types:str, value:str) -> any:
    """
    Conversion type

    :param types(str): Data type
    :param value(str): Value

    :return: any
    """

    func = data_type_mapping.get(types)

    return func(value) if func is not None else value
