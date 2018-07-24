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

def odd(n):
    if n % 2 == 1:
        a = (n+1) // 2
    else:
        a = n // 2
    return a

def bian1(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                grid[i][j]=1
    return grid

def shaixuan(Northlist):
    list_s=[]
    if Northlist != {}:
        for each in list(Northlist):
            if Northlist[each] == 0:
                del Northlist[each]
        for each1 in Northlist:
            list_s.append((each1,Northlist[each1]))
    
    return list_s

def panduan(n,grid):
    try:
        count_n=0
        n_len = len(n)
        for each in n:
            if grid[each[0]][each[1]] == 1:
                count_n += 1
            else:
                count_n += 0
        if n_len == count_n:
            return True
        else:
            return False
    except IndexError:
        return False

def North_list(grid):
    grid_len = len(grid)
    max_len = odd(grid_len)
    diction = {}
    if max_len >= 2:
        for each in range(2,max_len+1):
            diction[each] = 0
        for i in range(0,grid_len-1):
            for j in range(1,grid_len-1):
                if grid[i][j] == 1:
                    double_bra=[[i,j]]
                    a0=(i,j)
                    panduan1=panduan(double_bra,grid)
                    if panduan1:
                        single_answer=judge_N(a0,grid)
                    real_answer = single_answer+1
                    if real_answer >= 2:
                        diction[real_answer] += 1        
    return diction
def judge_N(a0,grid,L=1,count=1):
    a11=a0[0]
    b11=a0[1]
    if b11 > 0 :
        a12 = a11+1
        b12 = b11 - 1
        if a12 >= 0:
            n = L*2
            b13 =  n +1
            L += 1
            new =[]
            a1=(a12,b12)
            for each_element in range(0,b13):
                new.append([a12,b12+each_element])
            panduan2 = panduan(new,grid)  
            if panduan2:   
                return count + judge_N(a1,grid,L,count)
            else:
                return 0
        else:
            return 0
    else:
        return 0
def South_list(grid):
    grid_len = len(grid)
    max_len = odd(grid_len)
    diction = {}
    if max_len >= 2:
        for each in range(2,max_len+1):
            diction[each] = 0
        for i in range(1,grid_len)[::-1]:
            for j in range(1,grid_len-1):
                if grid[i][j] == 1:
                    double_bra=[[i,j]]
                    a0=(i,j)
                    panduan1=panduan(double_bra,grid)
                    if panduan1:
                        single_answer=judge_S(a0,grid)
                    real_answer = single_answer+1
                    if real_answer >= 2:
                        diction[real_answer] += 1        
    return diction
def judge_S(a0,grid,L=1,count=1):
    a11=a0[0]
    b11=a0[1]
    if b11 > 0 :
        
        a12 = a11-1
        b12 = b11 - 1
        if a11 >= 0:
            n = L*2
            b13 =  n +1
            L += 1
            new =[]
            a1=(a12,b12)
            for each_element in range(0,b13):
                new.append([a12,b12+each_element])
            panduan2 = panduan(new,grid)  
            if panduan2:   
                return count + judge_S(a1,grid,L,count)
            else:
                return 0
        else:
            return 0   
    else:
        return 0
def West_list(grid):
    grid_len = len(grid)
    max_len = odd(grid_len)
    diction = {}
    if max_len >= 2:
        for each in range(2,max_len+1):
            diction[each] = 0
        for i in range(0,grid_len-1):
            for j in range(1,grid_len-1):
                if grid[j][i] == 1:
                    double_bra=[[j,i]]
                    a0=(j,i)
                    panduan1=panduan(double_bra,grid)
                    if panduan1:
                        single_answer=judge_W(a0,grid)
                    real_answer = single_answer+1
                    if real_answer >= 2:
                        diction[real_answer] += 1        
    return diction
def judge_W(a0,grid,L=1,count=1):
    a11=a0[0]
    b11=a0[1]
    if a11 > 0 :

        a12 = a11 - 1
        b12 = b11 + 1
        n = L*2
        b13 =  n +1
        L += 1
        new =[]
        a1=(a12,b12)
        for each_element in range(0,b13):
            new.append([a12+each_element,b12])
        panduan2 = panduan(new,grid)  
        if panduan2:   
            return count + judge_W(a1,grid,L,count)
        else:
            return 0
    else:
        return 0
def East_list(grid):
    grid_len = len(grid)
    max_len = odd(grid_len)
    diction = {}
    if max_len >= 2:
        for each in range(2,max_len+1):
            diction[each] = 0
        for i in range(1,grid_len)[::-1]:
            for j in range(1,grid_len-1):
                if grid[j][i] == 1:
                    double_bra=[[j,i]]
                    a0=(j,i)
                    panduan1=panduan(double_bra,grid)
                    if panduan1:
                        single_answer=judge_E(a0,grid)
                    real_answer = single_answer+1
                    if real_answer >= 2:
                        diction[real_answer] += 1        
    return diction
def judge_E(a0,grid,L=1,count=1):
    a11=a0[0]
    b11=a0[1]
    if a11 > 0 :
        a12 = a11 - 1
        b12 = b11 - 1
        if b12 >= 0:
            n = L*2
            b13 =  n +1
            L += 1
            new =[]
            a1=(a12,b12)
            for each_element in range(0,b13):
                new.append([a12+each_element,b12])
            panduan2 = panduan(new,grid)  
            if panduan2:   
                return count + judge_E(a1,grid,L,count)
            else:
                return 0
        else:
            return 0
    else:
        return 0

def North(grid):
    N_list = North_list(grid)
    result = shaixuan(N_list)
    return result
def South(grid):
    S_list = South_list(grid)
    result = shaixuan(S_list)
    return result
def West(grid):
    W_list = West_list(grid)
    result = shaixuan(W_list)
    return result
def East(grid):
    E_list=East_list(grid)
    result = shaixuan(E_list)
    return result

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def triangles_in_grid(grid):
    grid1=bian1(grid)
    N=North(grid1)
    S=South(grid1)
    W=West(grid1)
    E=East(grid1)
    final_result={}
    if N != []:
        N1=N[::-1]
        final_result['N']=N1
    if E != []:
        E1=E[::-1]
        final_result['E']=E1
    if S != []:
        S1=S[::-1]
        final_result['S']=S1
    if W != []:
        W1=W[::-1]
        final_result['W']=W1
    return final_result
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
triangles = triangles_in_grid(grid)
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
