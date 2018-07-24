def add_up(L):
    s =0
    for e in L:
        s+=e
    return s
    
def add_up_1(L):
    if not L:
        return 0
    return add_up_1(L[: -1]) + L[-1]

def add_up_2(L):
    if not L:
        return 0
    return add_up_2(L[1: ]) + L[0]

def add_up_3(L):
    if not L:
        return 0
    if len(L)==1:
        return L[0]
    return add_up_3(L[: len(L)//2]) + add_up_3(L[len(L)//2 :])

    
    
        
