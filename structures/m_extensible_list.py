from typing import Generic, Optional, TypeVar

Datum = TypeVar("Datum")
"""Generic type for the payload of an extensible list."""

INITIAL_CAPACITY: int = 4
"""The initial capacity of a new list."""


class ExtensibleList(Generic[Datum]):
    def __init__(self):
        """Initialise an empty list with some initial capacity."""

        self._data = [None] * INITIAL_CAPACITY
        """The list's data."""

        self._size = 0
        """The number of non-empty elements in the list."""

        self._capacity = INITIAL_CAPACITY
        """The list's capacity."""

    def __str__(self) -> str:
        """Stringifies the list, including empty cells."""
        raise NotImplementedError()

    def __resize(self) -> None:
        """Increases the list size."""
        raise NotImplementedError()

    def reset(self) -> None:
        """Resets the list to its initial form."""
        raise NotImplementedError()

    def __getitem__(self, index: int) -> Datum:
        """Returns the element at the given index of the list's data."""
        raise NotImplementedError()

    def get_at(self, index: int) -> Optional[Datum]:
        """
        Returns the element at the given index of the list's data, similarly to
        `__getitem__`. If the index is outside the required bounds, returns `None`.
        """
        raise NotImplementedError()

    def __setitem__(self, index: int, element: Datum) -> None:
        """Sets the element at the given index of the list's data."""
        raise NotImplementedError()

    def set_at(self, index: int, element: Datum) -> None:
        """
        Sets the element at the given index of the list's data, similarly to
        `__setitem__`. If the index is outside the required bounds, does nothing.
        """
        raise NotImplementedError()

    def append(self, element: Datum) -> None:
        """Adds an element to the end of the list. Resizes the list where necessary."""
        raise NotImplementedError()

    def remove(self, element: Datum) -> None:
        """
        Removes the first instance of the given element. Ensures elements remain
        contiguous.
        """
        raise NotImplementedError()

    def remove_at(self, index: int) -> Optional[Datum]:
        """
        Removes and returns the element at the given index. If the index is outside the
        required bounds, returns `None`.
        """
        raise NotImplementedError()

    def is_empty(self) -> bool:
        """Returns whether the structure is empty."""
        return self.get_size() == 0

    def is_full(self) -> bool:
        """Returns whether the structure is full."""
        return self.get_size() == self.get_capacity()

    def get_size(self) -> int:
        """Returns the number of non-empty elements in the list."""
        return self._size

    def get_capacity(self) -> int:
        """Returns the total capacity of the list."""
        return self._capacity
