import os 
import sys
from copy import deepcopy
from collections import deque 
try:
    filename = input('Which data file do you want to use?')
    # filename = 'coast_1.txt'
    current_dir = os.getcwd()
    aim_dir = current_dir + '/' + filename
    file1 = open(aim_dir)
    file1.close()
except FileNotFoundError:
    print('No such file:filename')
    sys.exit()
with open(aim_dir) as data_file:
    aim_list=[each.strip().split(' ') for each in data_file.readlines()]
for each in aim_list:
    each[0] = int(each[0])
    each[1] = int(each[1])
# aim_list.sort(key=lambda x:x[1],reverse = True)
# print(aim_list)

aim_list_len = len(aim_list)
max_each = round(sum(each[1] for each in aim_list) / aim_list_len)
min_num = min(each[1] for each in aim_list)
first_num = round((max_each + min_num) / 2)
def result(aim_list,first_num,min_num,max_each):
    b=aim_list
    a=first_num
    min_num1= min_num
    max_each1= max_each

    aim_new_list = deepcopy(aim_list)
    
    aim_list_len = len(aim_list)
    for i in range(aim_list_len-1):
        if first_num < aim_list[i][1]:
            distance = abs(aim_list[i+1][0] - aim_list[i][0])
            got_fish = max(aim_list[i][1] - first_num - distance,0)
            aim_list[i+1][1] += got_fish
            aim_list[i][1] = first_num
        elif first_num == aim_list[i][1]:
            continue
        else:
            distance = abs(aim_list[i+1][0] - aim_list[i][0])
            got_fish = first_num - aim_list[i][1]
            aim_list[i+1][1] = aim_list[i+1][1] - distance - got_fish
            aim_list[i][1] = first_num

            
    if aim_list[-1][1] == first_num:
        return first_num
    elif aim_list[-1][1]>first_num:
        min_num1 = first_num
        return result(aim_new_list,round((first_num+max_each1)/2),min_num1,max_each1)
    else:
        max_each1 = first_num
        return result(aim_new_list,round((first_num+min_num1)/2),min_num1,max_each1)
        
max_quanti = result(aim_list,first_num,min_num,max_each)
print(f'The maximum quantity of fish that each town can have is {max_quanti}.')

  
    

