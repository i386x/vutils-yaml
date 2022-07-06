#
# File:    ./tests/unit/common.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2022-07-07 18:20:52 +0200
# Project: vutils-yaml: Working with YAML format
#
# SPDX-License-Identifier: MIT
#
"""Shared test code and data."""

from vutils.testing.utils import ClassLikeSymbol


class PySet(metaclass=ClassLikeSymbol):
    """PySet class."""

    __slots__ = ()


class PyList(metaclass=ClassLikeSymbol):
    """PyList class."""

    __slots__ = ()


class PyDict(metaclass=ClassLikeSymbol):
    """PyDict class."""

    __slots__ = ()


SYMBOLS = (
    "_T",
    PySet,
    PyList,
    PyDict,
    "_MarkType",
    "_NodeType",
    "_CtorType",
    "_CtorSpecType",
    "_CtorDecorType",
    "_StreamType",
    "_new_date",
    "_new_datetime",
    "_CtorFuncType",
)
SLOT = "__foo__"
VALUE = "bar:42"
