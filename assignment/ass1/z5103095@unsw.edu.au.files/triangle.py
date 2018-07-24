# Written by *** for COMP9021


# Insert your code here
import os 
import sys
from collections import deque 
try:
    filename = input('Which data file do you want to use? ')
    # filename = 'triangle_1.txt'
    current_dir = os.getcwd()
    aim_dir = current_dir + '/' + filename
    file1 = open(aim_dir)
    file1.close()
except FileNotFoundError:
    print('No such file:filename')
    sys.exit()

with open(aim_dir) as data_file:
    aim_list=[each.strip().replace(' ','') for each in data_file.readlines()]
aim_list_len = len(aim_list)
last_layer = aim_list[-1]
total_list=[]
for each_nb in last_layer:
    total_list.append([int(each_nb),deque([int(each_nb)]),1])

New_list=[]
total_list_len = len(total_list)
for i in range(total_list_len-1):
    if total_list[i][0] > total_list[i+1][0]:
        a1=total_list[i]
        a1[1]=deque(a1[1])
        New_list.append(list(a1))
    elif total_list[i][0] < total_list[i+1][0]:
        a2=total_list[i+1]
        a2[1]=deque(a2[1])
        New_list.append(list(a2))
    else:
        total_list[i][2] += 1
        a3=total_list[i]
        a3[1]=deque(a3[1])
        New_list.append(list(a3))

aim_list.reverse()
aim_list.pop(0)

def result(New_list,aim_list):
    
    if len(aim_list) == 1:
        New_list[0][0] += int(aim_list[0])
        New_list[0][1].appendleft(int(aim_list[0]))
        return New_list


    else:
        Newlist = New_list 
        aim_list_length = len(aim_list)
        num_str = aim_list[0]
        for i in range(aim_list_length):
            Newlist[i][0] += int(num_str[i])
            Newlist[i][1].appendleft(int(num_str[i]))
        
        New_list_len = len(Newlist)
        fake_new_list=[]
        for j in range(New_list_len-1):
            if Newlist[j][0] > Newlist[j+1][0]:
                a1 = New_list[j]
                a1[1]=deque(a1[1])
                fake_new_list.append(list(a1))
            elif Newlist[j][0] < Newlist[j+1][0]:
                a2 = New_list[j+1]
                a2[1]=deque(a2[1])
                fake_new_list.append(list(a2))
            else:
                a3 = New_list[j]
                a3[1]=deque(a3[1])
                Newlist[j][2] += Newlist[j+1][2]
                fake_new_list.append(list(a3))
        aim_list.pop(0)
        return result(fake_new_list,aim_list)
final_result=result(New_list,aim_list)

print(f'The largest sum is: {final_result[0][0]}')
print(f'The number of paths yielding this sum is: {final_result[0][2]}')
print(f'The leftmost path yielding this sum is: {list(final_result[0][1])}')
