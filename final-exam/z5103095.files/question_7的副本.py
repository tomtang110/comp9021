


def f(height):
    '''
    >>> f(1)
    0
    >>> f(2)
    101
     0
    >>> f(3)
    21012
     101
      0
    >>> f(5)
    432101234
     3210123
      21012
       101
        0
    >>> f(10)
    9876543210123456789
     87654321012345678
      765432101234567
       6543210123456
        54321012345
         432101234
          3210123
           21012
            101
             0
    >>> f(15)
    43210987654321012345678901234
     321098765432101234567890123
      2109876543210123456789012
       10987654321012345678901
        098765432101234567890
         9876543210123456789
          87654321012345678
           765432101234567
            6543210123456
             54321012345
              432101234
               3210123
                21012
                 101
                  0
    >>> f(26)
    543210987654321098765432101234567890123456789012345
     4321098765432109876543210123456789012345678901234
      32109876543210987654321012345678901234567890123
       210987654321098765432101234567890123456789012
        1098765432109876543210123456789012345678901
         09876543210987654321012345678901234567890
          987654321098765432101234567890123456789
           8765432109876543210123456789012345678
            76543210987654321012345678901234567
             654321098765432101234567890123456
              5432109876543210123456789012345
               43210987654321012345678901234
                321098765432101234567890123
                 2109876543210123456789012
                  10987654321012345678901
                   098765432101234567890
                    9876543210123456789
                     87654321012345678
                      765432101234567
                       6543210123456
                        54321012345
                         432101234
                          3210123
                           21012
                            101
                             0
    '''
    # Insert your code here
   
    for i in range(height):
        
        print(' '*i,end='')
        for j in range(height-i)[::-1]:
            a = 0
            a += j 
            if a < 10 :
                print(f'{a}',end='')
            else:
                while a >= 10:
                    a -= 10
                print(f'{a}',end='')
        for k in range(1,height-i):
            a=0
            a += k 
            if a < 10:
                print(f'{a}',end='')
            else:
                while a >= 10:
                    a -= 10
                print(f'{a}',end='')
        print('')

            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
