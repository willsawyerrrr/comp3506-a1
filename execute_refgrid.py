import argparse
import sys

from structures.m_extensible_list import ExtensibleList
from structures.m_single_linked_list import SingleLinkedList, SingleNode
from structures.m_stack import EStack, LStack


class RefGrid:
    """
    You may add fields to this structure, but you must use either the provided
    ExtensibleList or SingleLinkedList member functions to store and operate on your
    RefGrid. You may use other data structures within each function where necessary.
    """

    def __init__(self):
        """
        Data is stored in either linkedlist or extlist depending on which `read_to_*`
        function is called.
        """

        self.linkedlist: SingleLinkedList = SingleLinkedList()
        """The linked list representation of the RefGrid."""

        self.extlist: ExtensibleList = ExtensibleList()
        """The extensible list representation of the RefGrid."""

        self.rows: int = 0
        """The number of rows in the RefGrid."""

        self.len: int = 0
        """The length of each row in the RefGrid."""

    def read_to_linkedlist(self, input_file: str) -> None:
        """Reads a RefGrid file into the linked list."""
        with open(input_file) as f:
            first = True
            for line in f:
                self.rows += 1
                for character in line.strip():
                    self.linkedlist.insert_to_front(SingleNode(character))
                    if first:
                        self.len += 1
                first = False

        self.linkedlist.reverse()

    def read_to_extlist(self, input_file: str) -> None:
        """Reads a RefGrid file into the extensible list."""
        with open(input_file) as f:
            first = True
            for line in f:
                self.rows += 1
                for character in line.strip():
                    self.extlist.append(character)
                    if first:
                        self.len += 1
                first = False

    def stringify_linkedlist(self) -> str:
        """Converts the linked list to a string."""

        outstr = ""
        counter = 0
        current = self.linkedlist.get_head()

        while current != None:
            outstr += str(current.get_data())
            counter += 1
            if counter % self.len == 0:
                outstr += "\n"
            current = current.get_next()

        return outstr

    def stringify_extlist(self) -> str:
        """Converts the extensible list to a string."""
        return str(self.extlist)

    def stringify_spliced_linkedlist(self) -> str:
        """
        Converts a cut-and-spliced linked list by handling the variable row length of
        each sequence.
        """
        outstr = ""
        counter = 0
        row = 0
        end = self.extlist.get_at(row)
        current = self.linkedlist.get_head()

        while current != None:
            outstr += str(current.get_data())
            counter += 1
            if counter == end:
                outstr += "\n"
                row += 1
                if row < self.rows:
                    end += self.extlist.get_at(row)
            current = current.get_next()

        return outstr

    def reverse_seq(self, k):
        """
        Task 2.1, sequence reversal. You need to use/store your result in the
        linkedlist class member.
        """
        new_list = SingleLinkedList()

        for _ in range(k * self.len):
            new_list.insert_to_front(self.linkedlist.remove_from_front())

        stack = EStack()
        for _ in range(k * self.len, (k + 1) * self.len):
            stack.push(self.linkedlist.remove_from_front())

        while not stack.is_empty():
            new_list.insert_to_front(stack.pop())

        for _ in range((k + 1) * self.len, self.rows * self.len):
            new_list.insert_to_front(self.linkedlist.remove_from_front())

        new_list.reverse()
        self.linkedlist = new_list

    def cut_and_splice(self, pattern: str, plen: int, target: str, tlen: int) -> None:
        """
        Replaces all occurrences of pattern with target in the RefGrid, storing the
        result in the `linkedlist` member.
        """
        for _ in range(self.rows):
            self.extlist.append(self.len)

        replace_inc = tlen - plen
        match_len = 0
        before = None
        node = self.linkedlist.get_head()

        while node is not None:
            if node.get_data() == pattern[match_len]:
                match_len += 1
            else:
                match_len = 0
                before = node

            if match_len == plen:
                node = self.join(before, node.get_next(), target, tlen)
                self.linkedlist.set_size(self.linkedlist.get_size() + replace_inc)
                match_len = 0
                before = node

            node = node.get_next()

    def join(
        self,
        before: SingleNode | None,
        after: SingleNode | None,
        target: str,
        tlen: int,
    ) -> None:
        """
        Joins the target to the linked list.

        If both before and after are not None, target will be inserted between them.
        head -> ... -> before -> target[0] -> ... -> target[-1] -> after -> ... -> null

        If after is None, target[-1] will be the last node in the linked list.
        head -> ... -> before -> target[0] -> ... -> target[-1] -> null

        If before is None, target[0] will be the first node in the linked list.
        head -> target[0] -> ... -> target[-1] -> after -> ... -> null

        If both before and after are None, target will replace the entire linked list.
        head -> target[0] -> ... -> target[-1] -> null
        """
        node = SingleNode(target[0])

        if before is not None:
            before.set_next(node)
        else:
            self.linkedlist.set_head(node)

        for i in range(1, tlen):
            node.set_next(SingleNode(target[i]))
            node = node.get_next()

        node.set_next(after)
        return node

    def right(self, idx: int) -> int:
        """Returns the index to the right of idx or 0 if it is out of bounds."""
        if idx < 0 or idx % self.len == self.len - 1 or idx >= self.rows * self.len:
            return 0
        return idx + 1

    def below(self, idx: int) -> int:
        """Returns the index below idx or 0 if it is out of bounds."""
        if idx < 0 or idx >= (self.rows - 1) * self.len:
            return 0
        return idx + self.len

    def is_viable(self) -> bool:
        """Returns whether the RefGrid is viable for cloning."""
        my_stack = LStack()
        visited = SingleLinkedList()
        current = 0
        end = self.extlist.get_size() - 1
        base = self.extlist.get_at(current)
        my_stack.push(current)
        visited.insert_to_front(SingleNode(current))

        while not my_stack.empty() and current != end:
            current = my_stack.pop()
            right_idx = self.right(current)
            below_idx = self.below(current)

            if (
                right_idx != 0
                and self.extlist.get_at(right_idx) == base
                and not visited.find_element(right_idx)
            ):
                my_stack.push(right_idx)
                visited.insert_to_front(SingleNode(right_idx))

            if (
                below_idx != 0
                and self.extlist.get_at(below_idx) == base
                and not visited.find_element(below_idx)
            ):
                my_stack.push(below_idx)
                visited.insert_to_front(SingleNode(below_idx))

        return current == end


def validate_patterns(pattern: str, target: str) -> bool:
    """Returns whether the pattern and target are valid."""

    if len(pattern) <= 0 or len(pattern) > 4:
        print("Error: Pattern [" + pattern + "] is too short or too long.")
        return False

    if len(target) <= 0 or len(target) > 4:
        print("Error: Target [" + target + "] is too short or too long.")
        return False

    bases = ["a", "c", "g", "t"]
    for b in bases:
        if pattern.count(b) > 1 or target.count(b) > 1:
            print("Error: Only allowed one occurrences of each base.")
            return False

        pattern = pattern.replace(b, "")
        target = target.replace(b, "")

    if len(pattern) > 0 or len(target) > 0:
        print("Error: Illegal characters provided.")
        return False

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="COMP3506/7505 Assignment One: DNA-RefGrid"
    )
    parser.add_argument(
        "--refgrid",
        type=str,
        required=True,
        help="Path to refgrid file",
    )
    parser.add_argument(
        "--reverse-k",
        type=int,
        help="Reverse the k-th sequence.",
    )
    parser.add_argument(
        "--cut-and-splice",
        type=str,
        help="Cut and splice pattern P with T. Use format P:T (eg: --cut-and-splice gta:atcgc",
    )
    parser.add_argument(
        "--check-clone",
        action="store_true",
        help="Check if the RefGrid is viable for cloning.",
    )
    args = parser.parse_args()

    if len(sys.argv) == 1:  # no arguments passed
        parser.print_help()
        sys.exit(-1)

    my_refgrid = RefGrid()

    # Task 2.1: Reverse-k
    if args.reverse_k is not None:
        print("Testing reverse k with k =", args.reverse_k)
        my_refgrid.read_to_linkedlist(args.refgrid)
        my_refgrid.reverse_seq(args.reverse_k)
        print(my_refgrid.stringify_linkedlist(), end="")
        sys.exit(0)

    # Task 2.2 Cut and Splice
    if args.cut_and_splice is not None:
        pattern, target = args.cut_and_splice.split(":")
        if not validate_patterns(pattern, target):
            sys.exit(-1)
        print("Testing cut-and-splice with P =", pattern, "and T =", target)
        my_refgrid.read_to_linkedlist(args.refgrid)
        my_refgrid.cut_and_splice(pattern, len(pattern), target, len(target))
        print(my_refgrid.stringify_spliced_linkedlist(), end="")
        sys.exit(0)

    # Task 2.3 Cloning Viability
    if args.check_clone:
        # use the extlist to store the data based on Barry Malloc's implementation
        my_refgrid.read_to_extlist(args.refgrid)
        is_viable = my_refgrid.is_viable()
        print("Testing viability via L-Path:", is_viable)
        sys.exit(0)
