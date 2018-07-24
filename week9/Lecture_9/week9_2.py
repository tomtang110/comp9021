from stack_adt import *
from collections import defaultdict
from queue_adt import *
def tree():
    return defaultdict(tree)

our_tree=tree()
our_tree[1][2][3] = None
our_tree[1][4] = None
our_tree[1][5][6][7] = None
our_tree[1][5][6][8][9] = None
our_tree[1][5][6][10] = None
our_tree[1][5][11][12] = None
our_tree[1][5][13] = None
print(our_tree)
# our_tree ={1:[2,4,5],2:[3],5:[6,11,14],6:[7,8,10],8:[9],11:[12]}
def explore_tree_DFS(tree):
    stack=Stack()
    stack.push(([],tree))
    while not stack.is_empty():
        path,tree=stack.pop()
        print(path)
        if tree:
            for e in reversed(list(tree.keys())):
                stack.push((path+[e],tree[e]))

# bread first search
def explore_tree_BFS(tree):
    queue = Queue()
    queue.enqueue(([],tree))
    while not queue.is_empty():
        path,tree = queue.dequeue()
        print(path)
        if tree:
            print(tree.keys())
            for e in list(tree.keys()):
                queue.enqueue((path+[e],tree[e]))
explore_tree_BFS(our_tree)




                           

        
