import os
import sys
directory_name='names'
classified_directory_name=directory_name+'_classified'
if os.path.exists(classified_directory_name):
    print('classified_directory_name exist already')
    sys.exit()

os.mkdir(classified_directory_name)

male_directory_name=classified_directory_name + '/male'
female_directory_name=classified_directory_name + '/female'
os.mkdir(male_directory_name)
os.mkdir(female_directory_name)
for filename in os.listdir(directory_name):
    if not filename.endswith('.txt'):
        continue
        # opening 1 file for reading purposes
        # and 2 files for wriring purposes
    with open(directory_name+'/'+filename) as data_file,\
            open(male_directory_name+'/'+filename,'w') as male_file,\
                open(female_directory_name+'/'+filename,'w') as female_file:
                for line in data_file:
                    name,gender,count=line.split(',')
                    if gender == 'F':
                        print(','.join((name,count)),file=female_file)
                    else:
                        print(','.join((name,count)),file=male_file)


