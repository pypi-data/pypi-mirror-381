from __future__ import annotations

import operator
from typing import *

import setdoc
from keyalias import keyalias
from overloadable import Overloadable

from v440._utils import releaseparse
from v440._utils.ListStringer import ListStringer
from v440._utils.releaseparse import deleting, getting, setting

__all__ = ["Release"]


@keyalias(major=0, minor=1, micro=2, patch=2)
class Release(ListStringer):
    __slots__ = ()

    string: str
    data: tuple[int]
    major: int
    minor: int
    micro: int
    patch: int

    @setdoc.basic
    def __delitem__(self: Self, key: Any) -> bool:
        self._data = deleting.delitem(self.data, key)

    @setdoc.basic
    def __getitem__(self: Self, key: Any) -> bool:
        return getting.getitem(self.data, key)

    @Overloadable
    @setdoc.basic
    def __init__(self: Self, *args: Any, **kwargs: Any) -> bool:
        if len(args) <= 1 and len(kwargs) == 0:
            return True
        if "string" in kwargs.keys():
            return True
        return False

    @__init__.overload(True)
    def __init__(self: Self, string: Any = "0") -> None:
        self._data = ()
        self.string = string

    @__init__.overload(False)
    def __init__(self: Self, data: Iterable) -> None:
        self._data = ()
        self.data = data

    @setdoc.basic
    def __setitem__(self: Self, key: Any, value: Any) -> bool:
        self._data = setting.setitem(self.data, key, value)

    @classmethod
    def _data_parse(cls: type, value: list) -> Iterable:
        v: list = releaseparse.tolist(value, slicing="always")
        while v and v[-1] == 0:
            v.pop()
        return v

    def _format(self: Self, format_spec: str) -> str:
        i: Optional[int]
        if format_spec:
            i = int(format_spec)
        else:
            i = None
        l: list = self[:i]
        if len(l) == 0:
            l += [0]
        l = list(map(str, l))
        ans: str = ".".join(l)
        return ans

    def _init_setup(self: Self) -> None:
        self._data = ()

    @classmethod
    def _sort(cls: type, value: int) -> int:
        return value

    def _string_fset(self: Self, value: str) -> None:
        if value == "":
            self.data = ()
            return
        v: str = value
        v = v.replace("_", ".")
        v = v.replace("-", ".")
        self.data = v.split(".")

    def bump(self: Self, index: SupportsIndex = -1, amount: SupportsIndex = 1) -> None:
        i: int = operator.index(index)
        a: int = operator.index(amount)
        x: int = getting.getitem_int(self.data, i) + a
        self._data = setting.setitem_int(self.data, i, x)
        if i != -1:
            self.data = self.data[: i + 1]
