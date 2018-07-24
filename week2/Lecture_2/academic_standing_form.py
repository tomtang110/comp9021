# Created by Eric Martin for COMP9021


'''
Prompts the user for a student id (which can have or not a leading z),
and creates a copy of Academic_Standing_Interview_Form.pdf, named
zid_Academic_Standing_Interview_Form.pdf, including only the first two pages.

Prompts the user for family name, given names, program/plan, phone number,
and academic standing level. Based on the current date, determines the previous semester,
assumed to be the one when academic standing was not good and justifying this interview.
The submission date is supposed to be the current date.

Then asks the user to open Academic_Standing_Interview_Form.pdf, and expects him or her
to position the mouse above the student id field at most 4 seconds after he or she
has pressed Return. Fills the 8 fields on the first page for which the information
has been provided or derived, and puts the focus on the Reasons for poor performance field,
expecting the student to fill that field and select the types of issue, and expecting
the academic advisor to provide recommendations and comments.

Then expects the user to position the mouse above the program authority name field
at most 4 seconds after he or she has pressed Return. Fills that field and the
Submission date field below, again supposed to be the current date.

Finally, asks user to save the file and quits.
'''


import os.path
import sys
import os
import datetime
import time

import PyPDF2
import pyautogui


program_authority_name = 'Eric Martin'
sleeping_time = 4
original_form_name = 'Academic_Standing_Interview_Form.pdf'
if not os.path.isfile(original_form_name):
    print(f'I could not find {original_form_name}. Giving up...')
    sys.exit()
student_number = input('What is your student id? ')
if student_number.startswith('z'):
    student_number = student_number[1: ]
if not student_number.isdigit() or len(student_number) != 7:
    print('Incorrect student number, giving up...')
    sys.exit()
student_id = 'z' + str(student_number)
form_name = student_id + '_' + original_form_name
if os.path.isfile(form_name):
    print(f'There is already a file named {form_name}. Giving up...')
    sys.exit()
family_name = input('What is your family name? ')
given_names = input('What are your given names? ')
program = input('What is your program/plan? ')
phone_number = input('What is your phone number? ')
academic_standing_level = input('What is your academic standing level? ')
date = datetime.datetime.now()
# Assumes that academic standing interviews for poor results in session 1
# always and exclusively take place between June and September.
if 5 < date.month < 10:
    semester_and_year = 'Semester 1, ' + str(date.year)
else:
    semester_and_year = 'Semester 2, ' + str(date.year - 1)
submission_date = date.strftime('%d/%m/%y')   
try:
    with open(form_name, 'wb') as output_file:
        original_pdf = PyPDF2.PdfFileReader(original_form_name)
        new_pdf = PyPDF2.PdfFileWriter()
        new_pdf.addPage(original_pdf.getPage(0))
        new_pdf.addPage(original_pdf.getPage(1))
        new_pdf.write(output_file)
except FileNotFoundError:
    print(f'Could not open {form_name}. Giving up...')
    sys.exit()   
print(f'\nOpen the file {form_name}.')
print('When you are ready to position the mouse above the Student ID field')
input(f'within {sleeping_time} seconds (not moving the mouse then), press return... ')
time.sleep(sleeping_time)
student_id_field = pyautogui.position()
pyautogui.click(student_id_field[0], student_id_field[1], clicks = 2)
pyautogui.typewrite(student_id + '\t' +  family_name + '\t' + given_names + '\t' +  program + '\t' +
                                              phone_number + '\t' + academic_standing_level + '\t' +
                                           semester_and_year + '\t' * 3 + submission_date + '\t' * 9
                   )
print('\nI assume student has provided type of issue and reasons for poor performance,')
print('and advisor has provided recommendation and comments.')
print('When ready to position the mouse above the program authority name field')
input(f'within {sleeping_time} seconds, press return... ')
time.sleep(sleeping_time)
program_authority_name_field = pyautogui.position()
pyautogui.click(program_authority_name_field[0], program_authority_name_field[1], clicks = 2)
pyautogui.typewrite(program_authority_name + '\t' + submission_date)
print('\nNow save the form. Thanks!')
