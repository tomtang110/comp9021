import sys
from math import sqrt

def is_prime(n):
    abc=round(sqrt(n))
    count=0
    if n!=2:
        for i in range(2,abc+1):
            if n%i == 0:
                count+=1
    if count==0:
        return True
    else:
        return False
        
def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    L=[i for i in range(2,n)]
    L1=[]

    for each in L:
        if is_prime(each) == True:
            L1.append(each)
    largest_prime_strictly_smaller_than_n += L1[-1]
    print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
