# Written by *** for COMP9021


# Insert your code here
import os 
import sys
from copy import deepcopy
from collections import deque 
from collections import defaultdict
def findline(each,aim1_list,aim2_list):

    aim1_list_0 =aim1_list[0]
    if each == aim1_list_0[0]:
        aim3_list= deepcopy(aim2_list)
        return str(each)+','+findline(aim1_list_0[1],aim3_list,aim2_list)
    else:
        aim1_list.pop(0)
        if aim1_list != []:
            return ''+findline(each,aim1_list,aim2_list)
        else:
            return str(each)
def kaishi(each,aim1_list):
    total_list=[]
    first_es = sorted(aim1_list,key=lambda x:x[0]==each,reverse=True)
    count =0
    for k in first_es:
        if each == k[0]:
            count+=1
    last_list = deque(first_es[count:])
    front_list = first_es[:count]
    for each_element in front_list: 
        last_list.appendleft(each_element)
        total_list.append(list(last_list))
        last_list.popleft()
    return total_list


   
try:
    filename = input('Which data file do you want to use? ')
    # filename = 'partial_order_2.txt'
    current_dir = os.getcwd()
    aim_dir = current_dir + '/' + filename
    file1 = open(aim_dir)
    file1.close()
except FileNotFoundError:
    print('No such file:filename')
    sys.exit()
with open(aim_dir) as data_file:
    aim_list=[each.strip() for each in data_file.readlines()]
aim1_list=[]
for each_line in aim_list:
    aim1_list.append((int(each_line[2]),int(each_line[4])))

# find beginning and enging point
begin_p = set()
ending_p = set()
aim1_list_len = len(aim1_list)
find_dict = defaultdict(list)
for k in range(aim1_list_len):
    find_dict[k] = aim1_list[k]
for i in range(aim1_list_len):
    copy_list = [h for h in range(aim1_list_len) if h != i]
    count1 = 0
    count2 = 0
    for num in copy_list:
        if aim1_list[i][0] == find_dict[num][1]:
            count1 += 1
        if aim1_list[i][1] == find_dict[num][0]:
            count2 += 1
    if not count1:
        begin_p.add(aim1_list[i][0])
    if not count2:
        ending_p.add(aim1_list[i][1])
result = defaultdict(list)

for each in begin_p:
    obtain_list = kaishi(each,aim1_list)
    for each_e in obtain_list:
        result[each].append(findline(each,each_e,each_e))
final_outcome=set()
for  each_d in begin_p:
    outcome = result[each_d][0]
    for i in result[each_d]:
        if len(outcome) < len(i):
            outcome = i
    outcome_list=[int(i) for i in outcome.split(',')]   
    outcome_list_len = len(outcome_list)
    for i in range(outcome_list_len-1):
        final_outcome.add((outcome_list[i],outcome_list[i+1]))
# print(final_outcome)
correct_res = []
for every in aim1_list:
    if every in final_outcome:
        correct_res.append(every)


print('The nonredundant facts are:')
for each in correct_res:
    print('R'+str(each).replace(' ',''))
