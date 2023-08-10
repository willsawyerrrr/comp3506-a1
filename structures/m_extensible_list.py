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
        string_rep = "[ "

        first = True
        for i in range(self.get_capacity()):
            if not first:
                string_rep += ", "

            if i < self.get_size():
                string_rep += f"{self.get_at(i)}"
            else:
                string_rep += "EMPTY"

            first = False

        string_rep += " ]"
        return string_rep

    def __resize(self) -> None:
        """Increases the list's size."""
        # The new capacity is the old capacity plus 1/8 of the old capacity, plus 6,
        # rounded up to the nearest multiple of 4. This is the same factor used by the
        # CPython implementation of `list`.
        # See https://github.com/python/cpython/blob/bace59d8b8e38f5c779ff6296ebdc0527f6db14a/Objects/listobject.c#L62.
        new_capacity = (self.get_capacity() + (self.get_capacity() >> 3) + 6) & ~3
        new_data = [None] * new_capacity

        for i in range(self.get_size()):
            new_data[i] = self._data[i]

        self._capacity, self._data = new_capacity, new_data

    def reset(self) -> None:
        """Resets the list to its initial form."""
        self.__init__()

    def __getitem__(self, index: int) -> Datum:
        """Returns the element at the given index of the list's data."""
        return self._data[index]

    def get_at(self, index: int) -> Optional[Datum]:
        """
        Returns the element at the given index of the list's data, similarly to
        `__getitem__`. If the index is outside the required bounds, returns `None`.
        """
        if index < 0 or index >= self.get_size():
            return None

        return self.__getitem__(index)

    def __setitem__(self, index: int, element: Datum) -> None:
        """Sets the element at the given index of the list's data."""
        self._data[index] = element

    def set_at(self, index: int, element: Datum) -> None:
        """
        Sets the element at the given index of the list's data, similarly to
        `__setitem__`. If the index is outside the required bounds, does nothing.
        """
        if index < 0 or index > self.get_size():
            return

        self.__setitem__(index, element)

    def append(self, element: Datum) -> None:
        """Adds an element to the end of the list. Resizes the list where necessary."""
        if self.is_full():
            self.__resize()

        self.__setitem__(self.get_size(), element)
        self.set_size(self.get_size() + 1)

    def remove(self, element: Datum) -> None:
        """
        Removes the first instance of the given element. Ensures elements remain
        contiguous.
        """
        for i in range(self.get_size()):
            if self.get_at(i) == element:
                self.remove_at(i)
                return

    def remove_at(self, index: int) -> Optional[Datum]:
        """
        Removes and returns the element at the given index. If the index is outside the
        required bounds, returns `None`.
        """
        if index < 0 or index >= self.get_size():
            return None

        element = self.get_at(index)

        for i in range(index, self.get_size()):
            self.set_at(i, self.get_at(i + 1))

        self.set_size(self.get_size() - 1)
        return element

    def is_empty(self) -> bool:
        """Returns whether the structure is empty."""
        return self.get_size() == 0

    def is_full(self) -> bool:
        """Returns whether the structure is full."""
        return self.get_size() == self.get_capacity()

    def get_size(self) -> int:
        """Returns the number of non-empty elements in the list."""
        return self._size

    def set_size(self, size: int) -> None:
        """Sets the number of non-empty elements in the list."""
        self._size = size

    def get_capacity(self) -> int:
        """Returns the total capacity of the list."""
        return self._capacity

    def set_capacity(self, capacity: int) -> None:
        """Sets the total capacity of the list."""
        self._capacity = capacity
