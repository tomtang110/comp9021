# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''
from decimal import Decimal

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
from math import gcd
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
    decimal=str(result_float).split('.')
    integral_part+=result_int #integral part
    if decimal != 0:
        sigma+=decimal[1] #sigma
    else:
        sigma= ''
        

else:
    has_finite_expansion = False
    result_int=numerator1//denominator1
    result_float=numerator1/denominator1
    kuwa=str(result_float).split('.')
    decimal=kuwa[1]

    if numerator1>denominator1:
        
        numerator1 -= result_int * denominator1

    numerator_1=numerator1
    denominator_1=denominator1

    remainderlist=[]
    remainder1=numerator_1 % denominator_1
    remainderlist.append(remainder1)
    remainder2=remainder1 * 10 % denominator_1
    while remainder2 not in remainderlist:
        remainderlist.append(remainder2)
        remainder2=remainder2 * 10 % denominator_1
    remainderlist.append(remainder2)

    remainderlist_len=len(remainderlist)
    place=remainderlist.index(remainderlist[-1])
    repeating_part=[]

    for i in range(place,remainderlist_len-1):
        repeating_part.append(remainderlist[i])
    tau1=''
    for each in repeating_part:
        quotient=each*10//denominator_1
        tau += str(quotient)   #tau


    integral_part+=result_int   #integral_part
    sigma_list=decimal.split(tau)
    sigma+=sigma_list[0:]   #sigma



    


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

