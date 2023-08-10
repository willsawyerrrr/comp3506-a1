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

    def push(self, element: Datum) -> None:
        """Pushes the given element to the top of the stack."""
        raise NotImplementedError()

    def pop(self) -> Optional[Datum]:
        """
        Removes and returns the top element. If the stack is empty, returns `None`.
        """
        raise NotImplementedError()

    def peek(self) -> Optional[Datum]:
        """Returns the top element. If the stack is empty, returns `None`."""
        raise NotImplementedError()

    def empty(self) -> bool:
        """Returns whether the stack is empty."""
        raise NotImplementedError()

    # Hint: Override the required operations inherited from the ExtensibleList below
    #       which are needed to allow the EStack to function correctly. It is ok to
    #       implement push, pop and seek in terms of inherited functionality.


class LStack(Generic[Datum], SingleLinkedList[Datum]):
    """A stack implementation using the SingleLinkedList for object storage."""

    def __init__(self):
        """Creates an empty stack."""
        raise NotImplementedError()

    def push(self, element: Datum) -> None:
        """Pushes the given element to the top of the stack."""
        raise NotImplementedError()

    def pop(self) -> Optional[Datum]:
        """
        Removes and returns the top element. If the stack is empty, returns `None`.
        """
        raise NotImplementedError()

    def peek(self) -> Optional[Datum]:
        """Returns the top element. If the stack is empty, returns `None`."""
        raise NotImplementedError()

    def empty(self) -> bool:
        """Returns whether the stack is empty."""
        raise NotImplementedError()

    # Hint: Override the required operations inherited from the SingleLinkedList below
    #       which are needed to allow the LStack to function correctly. It is ok to
    #       implement push, pop and seek in terms of inherited functionality.
