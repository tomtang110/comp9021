import os 
import sys
try:
    # filename = input('Please input the filename:')
    filename = 'triangle_2.txt'
    current_dir = os.getcwd()
    aim_dir = current_dir + '/' + filename
    file1 = open(aim_dir)
    file1.close()
except FileNotFoundError:
    print('No such file:filename')
    sys.exit

with open(aim_dir) as data_file:
    aim_list=[each.strip().replace(' ','') for each in data_file.readlines()]
# print(aim_list)
i=0
j=0
def nb_of_tower(i,j,aim_list):
    aim_list_len = len(aim_list)
    if i == aim_list_len - 1:
        result = int(aim_list[i][j])
        return result
    else:
        first_nb = int(aim_list[i][j])
        result=first_nb+max(nb_of_tower(i+1,j,aim_list),nb_of_tower(i+1,j+1,aim_list))
        return result
result = nb_of_tower(i,j,aim_list)
print(result)

    

