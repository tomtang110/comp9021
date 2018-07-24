# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint


dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(grid[i][j]) for j in range(dim)))

# Possibly define other functions

try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

size_of_largest_homogenous_region_from_top_left_corner  = 0
# Replace this comment with your code
from copy import deepcopy
grid1 = deepcopy(grid)
def count_1(i,j,R):
    global grid
    if grid[i][j] == R:
        grid[i][j] = '*'
        if i:
            count_1(i-1,j,R)
        if i<dim -1:
            count_1(i+1,j,R)
        if j:
            count_1(i,j-1,R)
        if j < dim-1:
            count_1(i,j+1,R)
#question1
if  grid[0][0] == 1:
    count_1(0,0,1)
elif grid[0][0] == 0:
    count_1(0,0,0)    
size_top_lef=sum(i.count('*') for i in grid)
size_of_largest_homogenous_region_from_top_left_corner  += size_top_lef

        

print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = 0
# Replace this comment with your code
#question2


##grid[0][0]='*'
def count_2(i,j,grid,grid1,emp_list):
    ab=(i,j)
    if ab not in emp_list:
        emp_list.append(ab)
        grid[i][j] = '*'
        if i:
            if grid1[i][j] != grid1[i-1][j]:
                count_2(i-1,j,grid,grid1,emp_list)
        if i<dim - 1:
            if grid1[i][j] != grid1[i+1][j]:
                count_2(i+1,j,grid,grid1,emp_list)
        if j:
            if grid1[i][j] != grid1[i][j-1]:
                count_2(i,j-1,grid,grid1,emp_list)
        if j<dim - 1:
            if grid1[i][j] != grid1[i][j+1]:
                count_2(i,j+1,grid,grid1,emp_list)

q2=[]
for i in range(len(grid1)):
    for j in range(len(grid1)): 
        grid=deepcopy(grid1)  
        count_2(i,j,grid,grid1,[])
        answer = sum(k.count('*') for k in grid)
        q2.append(answer)
max_size_of_region_with_checkers_structure += max(q2)
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )

