# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Email:
# @Date:   2019-12-12 21:04:25
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-25 21:44:23
import os


from setuptools import setup, find_packages


with open('README.rst') as f:
    long_description = f.read()


def read_requirements(path: str) -> list:
    """
    read requirements/

    :param path(str): path

    :return: list
    """

    requires = []

    with open(path) as f:
        install_requires = f.read().split("\n")

        for ir in install_requires:
            if "-r" in ir:
                path = os.path.join(os.path.split(path)[0], ir.split(" ")[1])
                requires.extend(read_requirements(path))
            else:
                ir and requires.append(ir)

    return requires


setup(
    name="interact-cli",
    version="0.2.0",
    author="jankincai",
    author_email="jankincai12@gmail.com",
    maintainer="jankincai",
    maintainer_email="jankincai12@gmail.com",
    url="https://github.com/caizhengxin/interact-cli",
    download_url="https://github.com/caizhengxin/interact-cli.git",
    license="BSD",
    description="Interactive command line tool.",
    long_description=long_description,
    keywords=[
        "interact-cli",
        "interact",
        "cli",
    ],
    zip_safe=False,
    packages=find_packages(),
    install_requires=read_requirements("requirements/publish.txt"),
    include_package_data=True,  # MANIFEST.in
    project_urls={
        "Documentation": "https://interact-cli.readthedocs.io",
        "Source Code": "https://github.com/caizhengxin/interact-cli",
    },
    platforms="any",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
)
