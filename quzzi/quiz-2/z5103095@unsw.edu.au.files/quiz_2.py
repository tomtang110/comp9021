# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

# Replace this comment with your code
#repeating decimal
greatest_common_divi=gcd(numerator,denominator)
numerator1=numerator//greatest_common_divi
denominator1=denominator//greatest_common_divi

def primes_break(denominator1):
    if denominator1 == 1:
        return True
    
    while denominator1 % 5 == 0:
        denominator1 /= 5
        if denominator1 == 1:
            return True

    while denominator1 % 2 == 0:
        denominator1 /= 2
        if denominator1 == 1:
            return True
    
    return False

            

judge=primes_break(denominator1)
if judge == True:
    has_finite_expansion = True
    result_float=numerator/denominator
    result_int=numerator//denominator
    decimal=result_float-result_int
    integral_part+=result_int #integral part
    if decimal != 0:
        sigma+=str(decimal)[2:] #sigma
    else:
        sigma= ''
        

else:
    has_finite_expansion = False
    result_int=numerator1//denominator1
    result_float=numerator1/denominator1
    decimal=result_float-result_int

    if numerator1>denominator1:
        
        numerator1 -= result_int * denominator1

    numerator_1=numerator1
    denominator_1=denominator1

    remainderlist={}
    remainder1=numerator_1 % denominator_1
    while remainder1 not in remainderlist:

        quotient=remainder1 * 10 // denominator_1
        remainderlist[remainder1] = quotient
        remainder1 = remainder1*10 % denominator_1
    remainderlist.clear()
    while remainder1 not in remainderlist:

        quotient=remainder1 * 10 // denominator_1
        remainderlist[remainder1] = quotient
        remainder1 = remainder1*10 % denominator_1

    for each in remainderlist:
        
        tau += str(remainderlist[each])   #tau

    integral_part+=result_int   #integral_part
    sigma_list=str(decimal).split(tau)
    sigma+=sigma_list[0][2:]   #sigma






if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

