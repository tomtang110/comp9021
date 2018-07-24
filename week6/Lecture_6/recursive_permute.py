# Written by Eric Martin for COMP9021


'''
A recursive implementation of Heap's algorithms to generate the permutations of a list.
'''


def permute(L):
    yield from heap_permute(L, len(L))
    
def heap_permute(L, length):
    if length <= 1:
        yield L
    else:
        length -= 1
        for i in range(length):
            yield from heap_permute(L, length)
            if length % 2:
                L[i], L[length] = L[length], L[i]
            else:
                L[0], L[length] = L[length], L[0]
        yield from heap_permute(L, length)
