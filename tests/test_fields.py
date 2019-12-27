# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 20:52:19
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-27 23:52:02
from interact.fields import (
    IntField,
    ChoiceField,
    StringField,
    ListField,
    BooleanField,
)


def test_intfield():
    """
    default
    """

    assert IntField(default=40).is_default_valid() is True


def test_intfield_max():
    """
    Exceeded maximum
    """

    assert IntField(default=40, max_value=30).is_default_valid() is False


def test_intfield_min():
    """
    Within rage
    """

    assert IntField(default=30, min_value=20, max_value=40).is_default_valid() is True


def test_intfield_min_max():
    """
    Exceeded minimum
    """

    assert IntField(default=10, min_value=20).is_default_valid() is False


def test_booleanfield_false():
    """
    Boolean(False)
    """

    assert BooleanField(False).is_default_valid() is True


def test_booleanfield_true():
    """
    Boolean(True)
    """

    assert BooleanField(True).is_default_valid() is True


def test_booleanfield_failure():
    """
    Boolean(failure)
    """

    assert BooleanField("y").is_default_valid() is False


def test_strfield():
    """
    StringField
    """

    assert StringField("jan").is_default_valid() is True


def test_strfield_max():
    """
    StringField
    """

    assert StringField("jankincai", max_length=4).is_default_valid() is False


def test_strfield_min():
    """
    StringField
    """

    assert StringField("jan", min_length=4).is_default_valid() is False


def test_strfield_min_max():
    """
    StringField
    """

    assert StringField("jankincai", min_length=4, max_length=10).is_default_valid() is True


def test_strfield_regex_failure():
    """
    StringField
    """

    assert StringField("12", regex=r"^\d{2}$").is_default_valid() is True


def test_strfield_regex_success():
    """
    StringField
    """

    assert StringField("123", regex=r"^\d{2}$").is_default_valid() is False


def test_strfield_regex_min_max():
    """
    StringField
    """

    assert StringField("13", regex=r"^\d{2}$", min_length=1, max_length=4).is_default_valid() is True


def test_listfield():
    """
    ListField
    """

    assert ListField(["192.168.1.1"]).is_default_valid() is True


def test_listfield_min():
    """
    ListField
    """

    assert ListField(["192.168.1.1"], min_length=30).is_default_valid() is False


if __name__ == "__main__":
    test_intfield()
    test_intfield_max()
    test_intfield_min()
    test_intfield_min_max()
    test_booleanfield_false()
