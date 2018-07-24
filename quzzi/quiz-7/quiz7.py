# Generates a linked list of an even length of 4 or more, determined by user input,
# and reorders the list so that it starts with the first occurrence
# of the smallest element and repeatively moves backwards by one step and forward
# by three steps, wrapping around when needed.


import sys
from random import seed, randrange

from linked_list_adt import *
from extended_linked_list import ExtendedLinkedList


def collect_references(L, length):
    node = L.head
    references = set()
    for i in range(length):
        references.add(id(node))
        node = node.next_node
    return references


try:
    arg_for_seed, length = input('Enter 2 integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    # length: an even number at least equal to 4
    arg_for_seed, length = int(arg_for_seed), (abs(int(length)) + 2) * 2
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
L = [randrange(100) for _ in range(length)]

LL = ExtendedLinkedList(L)
LL.print()
references = collect_references(LL, length)
LL.rearrange()
if collect_references(LL, length) != references:
    print('You cheated!')
    sys.exit()
else:
    LL.print()
    