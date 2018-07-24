

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    # Insert your code here
    L_n=[]
    for each in word:
        bc = ord(each.upper())
        L_n.append(bc)
   
    L_n_len=len(L_n)
    L_s=[]
    L1=[]
    for i in range(L_n_len):
        if i == L_n_len-1:
            L1.append(L_n[i])
            L_s.append(L1)
        else:
            if L_n[i] == L_n[i+1]-1:
                L1.append(L_n[i])
            else:
                L1.append(L_n[i])
                L_s.append(L1)
                L1 = []
    length = 0
    
    for each in L_s:
        gg = len(each)
        if length < gg:
            length = gg
            bc=each
    
    acv=''
    desired_length += length
    for j in bc:
        acv += chr(j)

    desired_substring = acv.lower()
    
    
    
       
        
                
            
        
    
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
