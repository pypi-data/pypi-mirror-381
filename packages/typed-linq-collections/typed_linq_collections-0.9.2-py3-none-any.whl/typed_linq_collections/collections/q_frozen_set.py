from __future__ import annotations

from typing import TYPE_CHECKING, Never, override

from typed_linq_collections.q_iterable import QIterable

if TYPE_CHECKING:
    from collections.abc import Iterable

class QFrozenSet[TItem](frozenset[TItem], QIterable[TItem]):
    """An immutable set that extends Python's built-in frozenset with LINQ-style query operations.

    QFrozenSet provides all the functionality of Python's standard frozenset while also implementing
    the full QIterable interface for LINQ-style operations. It maintains all the performance
    characteristics and immutability of the built-in frozenset, making it a drop-in replacement
    that adds powerful querying capabilities.

    Being immutable, QFrozenSet instances are hashable and can be used as dictionary keys or
    stored in other sets. All LINQ operations return new collections rather than modifying
    the original.

    Inheritance:
    - Inherits from frozenset[TItem] for all standard immutable set operations and seamless interoperability with the built-in frozenset
    - Implements QIterable[TItem] for LINQ-style query operations

    Key Features:
    - **Immutable**: Cannot be modified after creation, ensuring thread safety
    - **Hashable**: Can be used as dictionary keys or set elements
    """
    __slots__: tuple[str, ...] = ()

    def __new__(cls, iterable: Iterable[TItem] = ()) -> QFrozenSet[TItem]:
        """Creates a new QFrozenSet with unique elements from the given iterable.

        Duplicate elements in the input iterable are automatically removed, maintaining
        only unique values as per standard frozenset behavior.

        Args:
            iterable: An iterable of elements to initialize the frozenset with.
                     Duplicates will be automatically removed.
                     Defaults to an empty sequence.

        Returns:
            A new QFrozenSet instance containing the unique elements from the iterable.
        """
        return super().__new__(cls, iterable)

    @override
    def _optimized_length(self) -> int: return len(self)

    _empty_set: QFrozenSet[Never]

    @staticmethod
    @override
    def empty() -> QFrozenSet[Never]:
        return QFrozenSet._empty_set


QFrozenSet._empty_set = QFrozenSet()  # pyright: ignore [reportGeneralTypeIssues, reportPrivateUsage]
