# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2020-01-15 11:09:52
# @Last Modified by:   JanKinCai
# @Last Modified time: 2020-01-17 14:36:06

SHOW_DEFAULT = 0
SHOW_LIGHTLIGHT = 1
SHOW_UNDERLINE = 4
SHOW_FLICKER = 5
SHOW_REVERSE = 7
SHOW_HIDE = 8

COLOR_BLACK = 30
COLOR_RED = 31
COLOR_GREEN = 32
COLOR_YELLOW = 33
COLOR_BLUE = 34
COLOR_FUCHSIA = 35
COLOR_CYAN_BLUE = 36
COLOR_WHITE = 37


def Color(vstr: str, color: int = None, background_color: int = None, show_type: int = None) -> str:
    """
    Color

    Args:
        param vstr: Format value.
        param color: Font color.
        param background_color: Background Color.
        param show_type: Show Type.

    Returns:
        str: Format value.
    """

    cv = []

    if show_type is not None:
        cv.append(str(show_type))

    if color is not None:
        cv.append(str(color))

    if background_color is not None:
        if background_color < 40:
            background_color += 10
        cv.append(str(background_color))

    cvs = ";".join(cv)

    return f"\033[{cvs}m{vstr}\033[0m"


def printc(values: str, color: int = None, background_color: int = None,
           show_type: int = None, *args, **kwargs):
    """print
    """

    print(Color(values, color, background_color, show_type), *args, **kwargs)


def inputc(values: str, color: int = None, background_color: int = None,
           show_type: int = None, *args, **kwargs) -> str:
    """input
    """

    return input(Color(values, color, background_color, show_type), *args, **kwargs)
