from __future__ import annotations

from typing import TYPE_CHECKING, override

# noinspection PyPep8Naming,PyProtectedMember
from typed_linq_collections._private_implementation_details.q_zero_overhead_collection_contructors import ZeroImportOverheadConstructors as C
from typed_linq_collections.collections.q_key_value_pair import KeyValuePair
from typed_linq_collections.q_iterable import QIterable

if TYPE_CHECKING:
    from collections.abc import Iterable

class QDict[TKey, TItem](dict[TKey, TItem], QIterable[TKey]):
    """A mutable dictionary that extends Python's built-in dict with LINQ-style query operations on keys.

    QDict provides all the functionality of Python's standard dictionary while also implementing
    the QIterable interface for LINQ-style operations on the dictionary keys. It maintains all
    the performance characteristics and mutability of the built-in dict, making it a drop-in
    replacement that adds powerful querying capabilities.

    Note that the QIterable operations work on the dictionary keys, not the values. Use the
    qitems() method to perform LINQ operations on key-value pairs.

    Inheritance:
    - Inherits from dict[TKey, TItem] for all standard dictionary operations and seamless interoperability with the built-in dict
    - Implements QIterable[TKey] for LINQ-style query operations on keys
    """
    __slots__: tuple[str, ...] = ()

    def __init__(self, elements: Iterable[tuple[TKey, TItem]] = ()) -> None:
        """Initializes a new QDict with key-value pairs from the given iterable.

        Args:
            elements: An iterable of (key, value) tuples to initialize the dictionary with.
                     Defaults to an empty sequence.
        """
        super().__init__(elements)

    def qitems(self) -> QIterable[KeyValuePair[TKey, TItem]]:
        """Returns a QIterable of KeyValuePair objects for LINQ operations on key-value pairs.

        This method provides access to both keys and values through KeyValuePair objects,
        enabling LINQ-style operations on the complete dictionary data. Each KeyValuePair
        has 'key' and 'value' properties for convenient access.

        Returns:
            A QIterable of KeyValuePair objects, each containing a key and its associated value.
        """
        return C.lazy_iterable(lambda: self.items()).select(KeyValuePair)

    @override
    def _optimized_length(self) -> int: return len(self)
