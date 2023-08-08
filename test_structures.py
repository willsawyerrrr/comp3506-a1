import argparse
import random
import sys
import time

from structures.m_extensible_list import ExtensibleList
from structures.m_single_linked_list import SingleLinkedList, SingleNode
from structures.m_stack import EStack, LStack


def test_single_linked_list():
    """Tests the implementation of the singly linked list."""
    print("==== Executing Single List Tests ====")

    my_single_list = SingleLinkedList()
    my_single_list.insert_to_front(SingleNode("hello"))
    my_single_list.insert_to_front(SingleNode("world"))
    my_single_list.insert_to_back(SingleNode("algorithms"))

    print(str(my_single_list))

    element = my_single_list.find_element("world")
    if element != None:
        print("Found node with data =", element.get_data())

    element = my_single_list.find_and_remove_element("woo")
    if element != None:
        print("Deleted", element.get_data())
    else:
        print("Didn't find element = woo")

    element = my_single_list.find_and_remove_element("world")
    if element != None:
        print("Deleted", element.get_data())
    else:
        print("Didn't find element = world")

    print(str(my_single_list))

    print("After 3 insertions and 1 deletion, size =", my_single_list.get_size())
    assert my_single_list.get_size() == 2


def test_extensible_list():
    """Tests the implementation of the extensible list."""
    print("==== Executing Extensible List Tests ====")
    my_ex_list = ExtensibleList()


def test_ex_stack():
    """Tests the implementation of the extensible list-based stack."""
    print("==== Executing Stack (ExtensibleList) Tests ====")
    my_stack = EStack()


def test_linked_stack():
    """Tests the implementation of the linked list-based stack."""
    print("==== Executing Stack (SingleLinkedList) Tests ====")
    my_stack = LStack()


def benchmark_stacks(n: int):
    """Times pushing and popping n random integers with both an EStack and an LStack."""
    es = EStack()
    ls = LStack()

    randomlist = random.choices(range(0, 100), k=n)

    t0 = time.time()
    for item in randomlist:
        es.push(item)
    while not es.empty():
        es.pop()
    t1 = time.time()
    total_es = t1 - t0

    t0 = time.time()
    for item in randomlist:
        ls.push(item)
    while not es.empty():
        ls.pop()
    t1 = time.time()
    total_ls = t1 - t0

    print("ExtensibleArray Stack:", total_es)
    print("SingleLinkedList Stack:", total_ls)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="COMP3506/7505 Assignment One: Data Structure Tests"
    )

    parser.add_argument(
        "--linked-list",
        action="store_true",
        help="Run linked list tests?",
    )
    parser.add_argument(
        "--ex-list",
        action="store_true",
        help="Run extensible list tests?",
    )
    parser.add_argument(
        "--linked-stack",
        action="store_true",
        help="Run stack (linked list) tests?",
    )
    parser.add_argument(
        "--ex-stack",
        action="store_true",
        help="Run stack (extensible list) tests?",
    )
    parser.add_argument(
        "--bench-stacks",
        type=int,
        help="Run stacks benchmark with k random integers.",
    )
    parser.set_defaults(stack=False, single_list=False, double_list=False)

    args = parser.parse_args()

    if len(sys.argv) == 1:  # no arguments passed
        parser.print_help()
        sys.exit(-1)

    if args.linked_list:
        test_single_linked_list()
    if args.ex_list:
        test_extensible_list()
    if args.linked_stack:
        test_linked_stack()
    if args.ex_stack:
        test_ex_stack()
    if args.bench_stacks is not None:
        benchmark_stacks(args.bench_stacks)
