from __future__ import annotations

from typed_linq_collections.collections.q_frozen_set import QFrozenSet


def test_q_frozen_set_empty_constructor() -> None:
    empty_set = QFrozenSet()
    assert len(empty_set) == 0
    assert empty_set.to_list() == []


def test_q_frozen_set_with_iterable() -> None:
    test_set = QFrozenSet([1, 2, 3, 2])  # Duplicates should be removed
    assert len(test_set) == 3
    assert set(test_set.to_list()) == {1, 2, 3}


def test_q_frozen_set_empty_static_method() -> None:
    empty_set = QFrozenSet.empty()
    assert len(empty_set) == 0
    assert empty_set.to_list() == []


def test_q_frozen_set_qcount() -> None:
    test_set = QFrozenSet([1, 2, 3])
    assert test_set.qcount() == 3

    empty_set = QFrozenSet()
    assert empty_set.qcount() == 0
