# Written by *** for COMP9021


# Insert your code here
import os 
import sys 
from collections import defaultdict
from copy import deepcopy
def single_pm_1(each_x,each_y,copy_list):
    for each_judge in copy_list:
        separat_judge=aim_dict[each_judge]
        if each_x in separat_judge[0] and each_y in separat_judge[1]:
            return False
        else:
            continue
    return True
def judge(read_list,copy_list,aim_dict,aim1_list):
    perimeter = 0
    count_block = 0
    for each_x in range(read_list[0],read_list[2]+1):
        each_y = read_list[1]
        single_pm1 = single_pm_1(each_x,each_y,copy_list)
        if single_pm1:
            perimeter += 1
            count_block = 0
        else:
            count_block += 1
        if count_block == 1:
            perimeter += 1
    for each_y in range(read_list[1]+1,read_list[3]+1):
        each_x = read_list[2]
        single_pm2 = single_pm_1(each_x,each_y,copy_list)
        if single_pm2:
            perimeter += 1
            count_block = 0
        else:
            count_block += 1
        if count_block == 1:
            perimeter += 1
      
    for each_x in range(read_list[0],read_list[2])[::-1]:
        each_y = read_list[3]
        single_pm1 = single_pm_1(each_x,each_y,copy_list)
        if single_pm1:
            perimeter += 1 
            count_block = 0
        else:
            count_block += 1
        if count_block == 1:
            perimeter += 1

    for each_y in range(read_list[1]+1,read_list[3])[::-1]:
        each_x = read_list[0]
        single_pm2 = single_pm_1(each_x,each_y,copy_list)
        if single_pm2:
            perimeter += 1 
            count_block = 0 
        else:
            count_block += 1
        if count_block == 1:
            perimeter += 1
    if count_block > 0:
        perimeter -= 1
         
    return perimeter
    
try:
    filename = input('Which data file do you want to use? ')
    # filename = 'frames_2.txt'
    current_dir = os.getcwd()
    aim_dir = current_dir + '/' + filename
    file1 = open(aim_dir)
    file1.close()
except FileNotFoundError:
    print('No such file:filename')
    sys.exit()

with open(aim_dir) as data_file:
    aim_list=[each.strip().split(' ') for each in data_file.readlines()]
aim1_list=[]
for each in aim_list:
    aim1_list.append([int(each[0]),int(each[1]),int(each[2]),int(each[3])])
# print(aim1_list)
aim_dict = defaultdict(list)
count = 0
aim1_list_len = len(aim1_list)
for k in range(aim1_list_len):
    aim_dict[count].append(range(aim1_list[k][0],aim1_list[k][2]+1))
    aim_dict[count].append(range(aim1_list[k][1],aim1_list[k][3]+1))
    count += 1
# print(aim_dict)
perimeter = 0
for j in range(aim1_list_len):
    copy_list = [k for k in range(aim1_list_len) if k != j]
    read_list = aim1_list[j]
    perimeter1 = judge(read_list,copy_list,aim_dict,aim1_list)
    perimeter +=perimeter1
print(f'The perimeter is: {perimeter}')
