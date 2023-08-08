from typing import Generic, Optional, TypeVar

Datum = TypeVar("Datum")
"""Generic type for the payload of a linked list."""


class SingleNode(Generic[Datum]):
    def __init__(self, data: Datum):
        """Initialise with some data and a null next pointer."""

        self._data: Optional[Datum] = data
        """Payload data of the node."""

        self._next: Optional[SingleNode[Datum]] = None
        """Pointer to the next node."""

    def set_data(self, data: Optional[Datum]) -> None:
        """Sets the payload data."""
        self._data = data

    def get_data(self) -> Optional[Datum]:
        """Gets the payload data."""
        return self._data

    def set_next(self, node: "Optional[SingleNode[Datum]]") -> None:
        """Sets the pointer to the next node."""
        self._next = node

    def get_next(self) -> "Optional[SingleNode[Datum]]":
        """Gets the pointer to the next node."""
        return self._next


class SingleLinkedList(Generic[Datum]):
    def __init__(self):
        """Initialize with no nodes and a size of zero."""

        self._head: Optional[SingleNode[Datum]] = None
        """The head of the list."""

        self._size: int = 0
        """The number of elements stored in the linked list."""

    def get_size(self) -> int:
        """Returns the number of elements stored in the linked list."""
        return self._size

    def set_size(self, size: int) -> None:
        """Sets the number of elements stored in the linked list."""
        self._size = size

    def get_head(self) -> Optional[SingleNode[Datum]]:
        """Returns the head element."""
        return self._head

    def set_head(self, node: Optional[SingleNode[Datum]]) -> None:
        """Sets the head element."""
        self._head = node

    def __str__(self) -> str:
        """Stringifies the list."""
        string_rep = ""
        current = self.get_head()

        while current is not None:
            # assumes the data stored in current has `__str__` implemented
            string_rep += str(current.get_data()) + " -> "
            current = current.get_next()

        string_rep += "[EOL]"  # end of list == None
        return string_rep

    def traverse_and_delete(self) -> None:
        """
        Deletes all of the elements in the list one-by-one. This is essentially a
        simulation, as with Python's memory management, we only need to remove reference
        to the head of the list to "delete" the linked list.
        """
        current = self.get_head()

        while current is not None:
            # get a handle on the next node
            next = current.get_next()
            # delete the reference to the next node
            current.set_next(None)
            # delete the data
            current.set_data(None)
            # move forward
            current = next

        # don't forget to remove the ref to the head node
        self.set_head(None)
        # and reset the size
        self.set_size(0)

    def insert_to_front(self, node: SingleNode) -> None:
        """Inserts a node to the front of the list."""
        if self.get_head() is not None:
            node.set_next(self.get_head())

        self.set_head(node)

    def insert_to_back(self, node: SingleNode) -> None:
        """Inserts a node to the back of the list."""
        current = self.get_head()

        # check corner case; the head is yet to be set
        if current is None:
            self.set_size(self.get_size() + 1)
            return

        # keep going until the next of the current node is empty
        while current.get_next() is not None:
            current = current.get_next()

        # we are now on the last valid node, let's insert
        current.set_next(node)
        self.set_size(self.get_size() + 1)

    def remove_from_front(self) -> Optional[SingleNode[Datum]]:
        """
        Removes and returns a node from the front of the list. If the list is empty,
        returns `None`.
        """
        if self.get_size() == 0:
            return None

        node = self.get_head()
        self.set_head(node.get_next())
        self.set_size(self.get_size() - 1)

        return node

    def remove_from_back(self) -> Optional[SingleNode[Datum]]:
        """
        Removes and returns a node from the back of the list. If the list is empty,
        returns `None`.
        """
        if self.get_size() == 0:  # nothing to remove
            return None

        if self.get_size() == 1:  # just the head element
            current = self.get_head()
            self.set_head(None)
            self.set_size(self.get_size() - 1)
            return current

        # more than one element - let's walk the list
        prev = None
        current = self.get_head()

        # keep going until the next of the current node is empty
        while current.get_next() is not None:
            prev = current
            current = current.get_next()

        prev.set_next(None)
        self.set_size(self.get_size() - 1)
        return current

    def find_element(self, element: Datum) -> Optional[SingleNode[Datum]]:
        """
        Finds and returns the element it if it exists. If the element is not in the
        list, returns `None`.
        """
        current = self.get_head()

        while current is not None:
            if current.get_data() == element:
                return current
            current = current.get_next()

        return None

    def find_and_remove_element(self, element: Datum) -> Optional[SingleNode[Datum]]:
        """
        Removes and returns the first instance of the element. If the element is not in
        the list, returns `None`.
        """
        previous = self.get_head()

        if previous == None:  # empty list - nothing to do
            return None

        current = previous.get_next()

        # corner case: if prev (head) is the element, we need to fix the head ptr
        if previous.get_data() == element:
            self.set_head(current)
            self.set_size(self.get_size() - 1)
            return previous

        while current is not None:  # walk the list
            if current.get_data() == element:  # we found it
                previous.set_next(current.get_next())
                self.set_size(self.get_size() - 1)
                return current

            # keep moving forward otherwise
            previous = current
            current = current.get_next()

        return None

    def reverse(self) -> None:
        """Reverses the list."""

        if self.get_head() is None:
            return

        if self.get_head().get_next() is None:
            return

        current = self.get_head()
        next = current.get_next()
        current.set_next(None)

        while next is not None:
            follow = next.get_next()
            next.set_next(current)
            current = next
            next = follow

        self.set_head(current)
