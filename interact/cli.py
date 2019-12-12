# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Date:   2019-12-12 22:37:50
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-12 23:16:06
import os
import sys
import argparse

from interact import __version__
from interact import loads


def main():
    """
    Interact cli
    """

    parser = argparse.ArgumentParser(description="Interact cli")
    parser.add_argument("-v", "--version", action="store_true", help="Show version.")
    args = parser.parse_args()
    # print("[+]:", args)

    if args.version:
        print(f"Interact cli version {__version__}")
        sys.exit(0)

    file = os.path.join(os.getcwd(), "interact.json")
    if not os.path.exists(file):
        print("Not found interact.json file.")
        sys.exit(1)

    print("=" * 60)
    print(loads(file))
    print("=" * 60)


if __name__ == "__main__":
    main()
