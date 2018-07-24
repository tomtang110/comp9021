

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
    word_list = [ord(i) for i in word]
    word_len = len(word_list)
    L = []
    L1 = []
    for i in range(word_len-1):
        if word_list[i] - word_list[i+1] == -1:
            L1.append(word_list[i])
        else:
            if L1 != []:
                L1.append(word_list[i])
                L.append(L1)
                L1 = []
                continue
            else:
                continue
    
    if L1 != []:
        if word_list[word_len-1]-word_list[word_len-2] == 1:
            L1.append(word_list[word_len-1])
        L.append(L1)
    if word_len == 1:
        L.append(word_list)
    ak = [len(o) for o in L]
    ak_max = max(ak)
    index1 = ak.index(ak_max)
    answer = L[index1]
    desired_substring = ''.join(chr(i) for i in answer)
    desired_length = len(answer)


    
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
