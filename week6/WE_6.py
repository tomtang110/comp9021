def permute(L):
    if len(L) <=1:
        yield L
    else:
        for i in range(len(L)):
            L[0],L[i]=L[i],L[0]
            for L1 in permute(L[1: ]):
                yield [L[0]] + L1
                
