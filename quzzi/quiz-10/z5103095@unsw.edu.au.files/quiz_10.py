# Implements the insertion into a priority queue
# with smallest elements being of highest priority
# as a binary tree.
#
# Written by Eric Martin for COMP9021


import sys
from random import randint, seed
from priority_queue import *


provided_input = input('Enter two integers, the second one nonnegative and at most equal to 10: ')
try:
    arg_for_seed, nb_of_nodes= provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
pq = PriorityQueue()
for _ in range(nb_of_nodes - 1):
    pq.insert(randint(0, nb_of_nodes))
    pq.print_binary_tree()
    print()
pq.insert(randint(0, nb_of_nodes))
pq.print_binary_tree()


