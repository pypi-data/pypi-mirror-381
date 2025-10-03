from __future__ import annotations

from typing import TYPE_CHECKING, override

from typed_linq_collections.q_iterable import QIterable

if TYPE_CHECKING:
    from collections.abc import Iterable


class QSet[TItem](set[TItem], QIterable[TItem]):
    """A mutable set that extends Python's built-in set with LINQ-style query operations.

    QSet provides all the functionality of Python's standard set while also implementing
    the full QIterable interface for LINQ-style operations. It maintains all the performance
    characteristics and uniqueness constraints of the built-in set, making it a drop-in
    replacement that adds powerful querying capabilities.

    Inheritance:
    - Inherits from set[TItem] for all standard set operations and seamless interoperability with the built-in set
    - Implements QIterable[TItem] for LINQ-style query operations
    """
    __slots__: tuple[str, ...] = ()

    def __init__(self, iterable: Iterable[TItem] = ()) -> None:
        """Initializes a new QSet with unique elements from the given iterable.

        Duplicate elements in the input iterable are automatically removed, maintaining
        only unique values as per standard set behavior.

        Args:
            iterable: An iterable of elements to initialize the set with.
                     Duplicates will be automatically removed.
                     Defaults to an empty sequence.
        """
        super().__init__(iterable)

    @override
    def _optimized_length(self) -> int: return len(self)

    @override
    def contains(self, value: TItem) -> bool:
        """Determines whether the set contains the specified element.

        This method provides O(1) average-case performance for membership testing,
        leveraging the underlying set's hash table implementation. It's part of the
        QIterable interface and provides a consistent API across all collection types.

        Args:
            value: The element to search for in the set.

        Returns:
            True if the element is found in the set, False otherwise.

        Examples:
            >>> qset = QSet([1, 2, 3, 4, 5])
            >>> qset.contains(3)
            True
            >>> qset.contains(10)
            False
            >>> # Equivalent to using 'in' operator
            >>> 3 in qset
            True
        """
        return value in self
