from __future__ import annotations

from collections.abc import Sequence
from typing import overload, override


class ImmutableSequence[TItem](Sequence[TItem]):
    __slots__: tuple[str, ...] = ("_items",)
    def __init__(self, items: Sequence[TItem] = ()) -> None:
        self._items: Sequence[TItem] = items  # Direct reference - no copying

    @override
    def __len__(self) -> int:
        return len(self._items)

    @overload
    def __getitem__(self, index: int) -> TItem: ...

    @overload
    def __getitem__(self, index: slice) -> ImmutableSequence[TItem]: ...

    @override
    def __getitem__(self, index: int | slice) -> TItem | ImmutableSequence[TItem]:
        if isinstance(index, slice):
            return ImmutableSequence(self._items[index])
        return self._items[index]

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Sequence):
            return False
        if len(self) != len(other):  # pyright: ignore [reportUnknownArgumentType]
            return False
        return all(self_item == other_item for self_item, other_item in zip(self._items, other, strict=False))  # pyright: ignore [reportUnknownArgumentType, reportUnknownVariableType]

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self._items)!r})"
