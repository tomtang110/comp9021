# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def leftmost_longest_path_from_top_left_corner(grid):
   
    if grid[0][0] == 0:
        return []
    else:
        i, j = 0, 0
        queue = Queue()
        queue.enqueue(([(i,j)]))
        grid_len = len(grid)
        while not queue.is_empty():
            road1= queue.dequeue()
            si_coo=road1[-1]
            i = si_coo[0]
            j = si_coo[1]
            if len(road1) == 1 or road1[-1][0] == road1[-2][0]:
                if len(road1) == 1 or road1[-1][1] - 1 == road1[-2][1]:
                    h = i - 1
                    g = j + 1
                    k = i + 1
                else:
                    h = i + 1
                    g = j - 1
                    k = i - 1
                if 0 <=k < grid_len:       
                    if (k,j) not in road1:
                        branch2 = grid[k][j]
                        if branch2 == 1:
                            queue.enqueue((road1+[(k,j)]))
                    
                if 0 <= g < grid_len:
                    if (i,g) not in road1:
                        branch1 = grid[i][g]
                        if branch1 == 1:
                            queue.enqueue((road1+[(i,g)]))
                    
                if grid_len>h >= 0:
                    if (h,j) not in road1:
                        branch4 = grid[h][j]
                        if branch4 == 1:
                            queue.enqueue((road1+[(h,j)]))
                    

            elif road1[-1][1] == road1[-2][1]:

                if road1[-1][0] == road1[-2][0] + 1:
                    h = j + 1
                    g = i + 1
                    k = j - 1
                else:
                    h = j - 1
                    g = i - 1
                    k = j + 1
                if 0 <=k < grid_len:       
                    if (i,k) not in road1:
                        branch2 = grid[i][k]
                        if branch2 == 1:
                            queue.enqueue((road1+[(i,k)]))
            
                if 0 <= g < grid_len:
                    if (g,j) not in road1:
                        branch1 = grid[g][j]
                        if branch1 == 1:
                            queue.enqueue((road1+[(g,j)]))
                if grid_len>h >= 0:
                    if (i,h) not in road1:
                        branch4 = grid[i][h]
                        if branch4 == 1:
                            queue.enqueue((road1+[(i,h)])) 
                        
                    

        return road1



    # Replace pass above with your code


provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner(grid)
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')
           
