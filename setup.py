# -*- coding: utf-8 -*-
# @Author: JanKinCai
# @Email:
# @Date:   2019-12-12 21:04:25
# @Last Modified by:   JanKinCai
# @Last Modified time: 2019-12-24 23:17:14
import os


from setuptools import setup, find_packages


with open('README.rst') as f:
    long_description = f.read()


def read_requirements(path):
    """
    递归读取requirements

    :param path: path
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
    version="0.1.0",
    author="jankincai",
    author_email="jankincai12@gmail.com",
    maintainer="jankincai",
    maintainer_email="jankincai12@gmail.com",
    url="https://github.com/caizhengxin/interact-cli",
    download_url="https://github.com/caizhengxin/interact-cli.git",
    license="BSD",
    description="Interact cli.",
    long_description=long_description,
    keywords=[
        "interact-cli",
        "interact",
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
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
