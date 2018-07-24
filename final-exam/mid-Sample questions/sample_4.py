
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    # Insert your code here

# Possibly define other functions
    sum1=0
    sum1_list=[]
    for i in range(n):
        k=sum(square[i])
        sum1_list.append(k)
        
    for p in range(n):
        for q in range(n):
            sum1 += square[q][p]
        sum1_list.append(sum1)
        sum1 =0

    for h in range(n):
        sum1 += square[h][h]
    sum1_list.append(sum1)
    sum1=0

    for g in range(n):
        sum1 += square[g][n-1-g]
    sum1_list.append(sum1)

    sum1_list_len = len(sum1_list)
    sum1_set_len = len(set(sum1_list))
    if sum1_list_len == sum1_set_len:
        return True
    else:
        return False
        
            

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
