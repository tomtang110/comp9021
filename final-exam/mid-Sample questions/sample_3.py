import sys
from math import sqrt

def is_prime(n):
    ab = round(sqrt(n))+1
    count = 0
    for i in range(2,ab):
        if n%i == 0:
            count += 1
    if count > 0:
        return False
    else:
        return True
            
        
def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    # Insert your code here
    L_1=[k for k in range(a,b+1) if is_prime(k)==True]
    L_1_len = len(L_1)
    a=0
    if L_1_len>1:
        for i in range(L_1_len-1):
            k=L_1[i+1]-L_1[i]-1
            if k>a:
                a = k
    max_gap = a
    
        
        
    
    
    print('The maximum gap between successive prime numbers in that interval is', max_gap)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
