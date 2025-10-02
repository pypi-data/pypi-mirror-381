# -*- coding: utf-8 -*-
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')
class Stack(Generic[T]):
    """栈"""
    _l: List[T] = []

    def __init__(self) -> None:
        self._l = []

    def pop(self) -> Optional[T]:
        if self.empty: return None
        return self._l.pop()

    def push(self, item: T) -> None:
        self._l.append(item)

    @property
    def empty(self) -> bool:
        return len(self._l) == 0

    @property
    def size(self) -> int:
        return len(self._l)

    @property
    def peak(self) -> Optional[T]:
        if self.empty: return None
        return self._l[-1]

    @property
    def data(self) -> List[T]:
        return self._l