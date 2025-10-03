from __future__ import annotations

import operator
from typing import *

from overloadable import Overloadable

from v440._utils.releaseparse import listing, numerals, ranging


def setitem(data: tuple, key: Any, value: Any) -> tuple:
    ans: tuple
    if type(key) is slice:
        k: range = ranging.torange(key, len(data))
        ans = setitem_range(data, k, value)
    else:
        i: int = operator.index(key)
        ans = setitem_int(data, i, value)
    return ans


def setitem_int(data: tuple, key: int, value: Any) -> tuple:
    v: int = numerals.numeral(value)
    if key < len(data):
        edit: list = list(data)
        edit[key] = v
        return tuple(edit)
    if v == 0:
        return data
    data += (0,) * (key - len(data))
    data += (v,)
    return data


@Overloadable
def setitem_range(data: tuple, key: range, value: Any) -> bool:
    return key.step == 1


@setitem_range.overload(False)
def setitem_range(data: tuple, key: range, value: Any) -> tuple:
    key: list = list(key)
    value: list = listing.tolist(value, slicing=len(key))
    if len(key) != len(value):
        e = "attempt to assign sequence of size %s to extended slice of size %s"
        e %= (len(value), len(key))
        raise ValueError(e)
    ext: int = max(0, max(*key) + 1 - len(data))
    edit: list = list(data)
    edit += [0] * ext
    for k, v in zip(key, value):
        edit[k] = v
    return tuple(edit)


@setitem_range.overload(True)
def setitem_range(data: tuple, key: range, value: Any) -> tuple:
    edit: list = list(data)
    ext: int = max(0, key.start - len(data))
    edit += ext * [0]
    l: list = listing.tolist(value, slicing="always")
    edit = edit[: key.start] + l + edit[key.stop :]
    return tuple(edit)
