from typing import Generic, Optional, TypeVar

from structures.m_extensible_list import ExtensibleList
from structures.m_single_linked_list import SingleLinkedList, SingleNode

Datum = TypeVar("Datum")
"""Generic type for the payload of a stack."""


class EStack(Generic[Datum], ExtensibleList[Datum]):
    """A stack implementation using the ExtensibleList for object storage."""

    def __init__(self):
        """Creates an empty stack."""
        super().__init__()

    def __str__(self) -> str:
        """Stringifies the stack."""
        string_rep = ""

        first = True
        for i in range(self.get_size() - 1, -1, -1):
            if first:
                string_rep += "[> "
            else:
                string_rep += ", "

            string_rep += str(self.get_at(i))

            if first:
                string_rep += " <]"

            first = False

        return string_rep

    def push(self, element: Datum) -> None:
        """Pushes the given element to the top of the stack."""
        self.append(element)

    def pop(self) -> Optional[Datum]:
        """
        Removes and returns the top element. If the stack is empty, returns `None`.
        """
        return self.remove_at(self.get_size() - 1)

    def peek(self) -> Optional[Datum]:
        """Returns the top element. If the stack is empty, returns `None`."""
        return self.get_at(self.get_size() - 1)

    def empty(self) -> bool:
        """Returns whether the stack is empty."""
        return self.is_empty()

    def remove(self, element: Datum) -> None:
        raise NotImplementedError()

    def reset(self) -> None:
        raise NotImplementedError()

    def set_capacity(self, capacity: int) -> None:
        raise NotImplementedError()


class LStack(Generic[Datum], SingleLinkedList[Datum]):
    """A stack implementation using the SingleLinkedList for object storage."""

    def __init__(self):
        """Creates an empty stack."""
        super().__init__()

    def push(self, element: Datum) -> None:
        """Pushes the given element to the top of the stack."""
        self.insert_to_front(element)

    def pop(self) -> Optional[Datum]:
        """
        Removes and returns the top element. If the stack is empty, returns `None`.
        """
        return self.remove_from_front()

    def peek(self) -> Optional[Datum]:
        """Returns the top element. If the stack is empty, returns `None`."""
        return self.get_head()

    def empty(self) -> bool:
        """Returns whether the stack is empty."""
        return self.get_head() is None

    def traverse_and_delete(self) -> None:
        raise NotImplementedError()

    def insert_to_back(self, node: SingleNode) -> None:
        raise NotImplementedError()

    def remove_from_back(self) -> SingleNode[Datum] | None:
        raise NotImplementedError()

    def find_element(self, element: Datum) -> SingleNode[Datum] | None:
        raise NotImplementedError()

    def find_and_remove_element(self, element: Datum) -> SingleNode[Datum] | None:
        raise NotImplementedError()

    def reverse(self) -> None:
        raise NotImplementedError()
