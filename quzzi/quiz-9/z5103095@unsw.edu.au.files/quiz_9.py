# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *

# Possibly define some functions


def left_recursive(tree,node_list):
    # print(tree.value)
    # print(node_list)
    right_node_t = tree.right_node
    # print(right_node_t.value)
    left_node_t = tree.left_node
    # print(left_node_t.value)
    if left_node_t.value == None and right_node_t.value == None:
        node1 = tree.value 
        if isinstance(node1,int):
            node_list.append(node1) 
    else:
        if left_node_t.value != None:
            left_recursive(left_node_t,node_list)
            if right_node_t.value != None:
                left_recursive(right_node_t,node_list)
            return node_list
        if right_node_t.value != None:
            left_recursive(right_node_t,node_list)
            if left_node_t.value != None:
                left_recursive(left_node_t,node_list)
            return node_list

    return node_list

        
def max_diff_in_consecutive_leaves(tree):
    if tree.value == None:
        return 0 
    node_list = left_recursive(tree,[])
    node_list_len = len(node_list)
    max_value = 0
    for k in range(node_list_len-1):
        difference = abs(node_list[k]-node_list[k+1])
        if max_value < difference:
            max_value = difference
    return max_value

    
    # Replace pass above with your code


provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
