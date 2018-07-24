import os
import sys
from collections import defaultdict
directory_name='names'
year_by_name=defaultdict(list)
for filename in os.listdir(directory_name):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3:7])
        # opening 1 file for reading purposes
        # and 2 files for wriring purposes
    with open(directory_name+'/'+filename) as data_file:
        for line in data_file:
            name,gender,count=line.split(',')
            if gender == 'M':
                break
            year_by_name[name].append(year)
        
for gap,starting_year,name in sorted([(year_by_name[name][i+1] - year_by_name[name][i],
     year_by_name[name][i],name) for name in year_by_name for i in range(len(year_by_name[name])-1)],reverse =True)[:10]:
        print(f'{name} was given in {starting_year}, and then {gap} years later')