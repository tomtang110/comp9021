import sys
from math import sqrt

def isP(n):
    if n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
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
    gap = []
    # Insert your code here
    primeList = []
    for i in range(a, b + 1):
        if isP(i):
            primeList.append(i)
        
    if len(primeList) >= 2:       
        temp = []
        for p, q in zip(primeList[:-1], primeList[1:]):
            temp.append(q - p)
        res = max(temp) - 1
        print(f'The maximum gap between successive prime numbers in that interval is {res}')
    else:
        print('The maximum gap between successive prime numbers in that interval is 0')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
