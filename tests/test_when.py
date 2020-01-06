# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-24 12:55:30
# @Last Modified by:   JanKinCai
# @Last Modified time: 2020-01-06 22:41:34
from interact.when import When


test_items = {
    "a": True,
    "b": "ssss",
    "c": 22,
    "d": {
        "dd": 23
    },
}


def test_true():
    """
    Test when boolean
    """

    vstr = "a == true"

    assert When(wv=vstr, cid=test_items).do_when() is True


def test_false():
    """
    Test when boolean
    """

    vstr = "a == false"

    assert When(wv=vstr, cid=test_items).do_when() is False


def test_str():
    """
    Test when str
    """

    vstr = "b == 'ssss'"

    assert When(wv=vstr, cid=test_items).do_when() is True


def test_str2():
    """
    Test when str
    """

    vstr = "b == ssss"

    assert When(wv=vstr, cid=test_items).do_when() is True


def test_str3():
    """
    Test when str
    """

    vstr = 'b == "ssss"'

    assert When(wv=vstr, cid=test_items).do_when() is True


def test_int():
    """
    Test when int
    """

    vstr = "c == 22"

    assert When(wv=vstr, cid=test_items).do_when() is True


def test_int2():
    """
    Test when int
    """

    vstr = "d.dd == 23"

    assert When(wv=vstr, cid=test_items).do_when() is True


def test_int3():
    """
    Test when int
    """

    vstr = "d.dd != 23"

    assert When(wv=vstr, cid=test_items).do_when() is False


def test_linux():
    """Test linux
    """

    assert When(wv="islinux", cid=test_items).do_when() is True


if __name__ == "__main__":
    test_true()
    test_false()
    test_str()
    test_str2()
    test_str3()
    test_int()
    test_int2()
    test_int3()
    test_linux()
