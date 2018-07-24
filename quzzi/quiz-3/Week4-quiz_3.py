# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict
def judge(A,grid,emptyL):
    for each in A:
        a=each[0]+1,b=each[1]-1
        
        
            
        else:
            return False  

def one(grid):
    
    for i in range(0,grid_len-1):
        for j in range(1,grid_len-1):
            triangle_list=[]
            examine_con=True
            A=[[i,j]]
            record_i = i
            record_j = j
            while examine_come:
                lay_judge_1=judge(A,grid)
                if lay_judge_1 == True:
                    record_i += 1
                    A=[]
                    B=[[record_i,record_j]]
                    
                    lay_judge_1 = judge(B,grid)
                    
                    if lay_judge_1 == True:
                        A.append([record_i,record_j])
                        record_j_1 = record_j - 1
                        record_j_2 = record_j + 1

                        C=[[record_i,record_j_1],[record_i,record_j_2]]
                        triangle_list.append(1)
                        A=[[i+1,j-1],[i+1,j],[i+1,j+1]]
                    else:
                        break
                else:
                    break





def odd(n):
    if n % 2 =1:
        a = (n+1) / 2
    else:
        a = n/2
    return a

def East(grid):

    grid_len = len(grid)

    if grid_len >2:
        max_size = odd(grid_len)
    else:
        max_size = 0
    
    for i in range(0,grid_len-1):
        for j in range(1,grid_len-1):
            if grid[i][j] == 1:
                C=[[i,j]]
    
                if grid[i+1][j] == 1:
                    a, c=b-1, d=b+1
                    if grid[i+1][j-1] == 1 and grid[i+1][j+1] == 1:
                        trangle_size.append(1)
                        a+=1 , b
                        if grid[i+1+1][j] == 1 :
                            c = b-1, d=b+1
                            if grid[i+1+1][j-1] == 1 and grid[i+1+1][j+1] == 1:
                                c -= 1, d+=1
                                if grid[i+1+1][j-1-1]==1 and grid[i+1+1][j+1+1] == 1:
                




def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def triangles_in_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                grid[i][j]=1
    

    return {}
    # Replace return {} above with your code

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
