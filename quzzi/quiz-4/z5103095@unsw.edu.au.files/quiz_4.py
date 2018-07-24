# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by *** and Eric Martin for COMP9021


import os


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Replace this comment with your code
from collections import defaultdict
# list the current directory
current_dir=os.getcwd()
aim_directory = current_dir+'/'+ directory
years_F_name = defaultdict(list)
years_M_name = defaultdict(list)
years_F_name[first_name] = [0,None]
years_M_name[first_name] = [0,None] 
for filename in os.listdir(aim_directory):
    if not filename.endswith('.txt'):
        continue
    else:
        years=int(filename[3:7])
        # years_F_name[first_name][1] = years
        # years_M_name[first_name][1] = years

        with open(aim_directory+'/'+filename) as data_file:
            female_tot_nb = 0
            male_tot_nb = 0
            firstname_f_nb = 0
            firstname_m_nb = 0
            for line in data_file:
                name, gender, number = line.split(',') 
                if gender == 'F':
                    female_tot_nb += int(number)
                    if name == first_name:
                        firstname_f_nb += int(number)
                else:
                    male_tot_nb += int(number)
                    if name == first_name:
                        firstname_m_nb += int(number)
            if years_F_name[first_name][0] < firstname_f_nb / female_tot_nb:
                years_F_name[first_name][0] = firstname_f_nb / female_tot_nb
                years_F_name[first_name][1] = years

            if years_M_name[first_name][0] < firstname_m_nb / male_tot_nb:
                years_M_name[first_name][0] = firstname_m_nb / male_tot_nb
                years_M_name[first_name][1] = years

if years_F_name[first_name][0] > float(0):
    female_first_year = years_F_name[first_name][1]
    min_female_frequency += years_F_name[first_name][0] * 100
if years_M_name[first_name][0] > float(0):
    male_first_year = years_M_name[first_name][1]
    min_male_frequency += years_M_name[first_name][0] * 100
	
if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

