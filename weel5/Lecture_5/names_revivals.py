# Written by Eric Martin for COMP9021


'''
Determines from National Data on the relative frequency of given names
in the population of U.S. births the top 10 names that have disappeared
and reappeared for the longest period of time.
The data are stored in a directory "names", in files named "yobxxxx.txt
with xxxx (the year of birth) ranging from 1880 to 2013.
'''


import os
import sys
from collections import defaultdict


directory = 'names'
if not os.path.exists(directory):
    print(f'There is no directory named {directory}, giving up...')
    sys.exit()
# A dictionnary where a key is a name and a value is the list
# of all years when the name was given.
years_per_name = defaultdict(list)
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    year = int(filename[3: 7])
    with open(directory + '/' + filename) as file:
        for line in file:
            name = line.split(',')[0]
            years_per_name[name].append(year)
# A list of triples consisting of:
# - difference between year when a name was last given and first given again,
# - year when name was last given,
# - name.
revivals = [[years_per_name[name][i + 1] - years_per_name[name][i], years_per_name[name][i], name]
                            for name in years_per_name for i in range(len(years_per_name[name]) - 1)
           ]
revivals.sort(reverse = True)
for i in range(10):
    print(f'{revivals[i][2]} was last used in {revivals[i][1]} and then again '
                              f'in {revivals[i][1] + revivals[i][0]}, {revivals[i][0]} years later.'
         )
