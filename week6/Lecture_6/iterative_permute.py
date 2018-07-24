# Written by Eric Martin for COMP9021


'''
An iterative implementation of Heap's algorithms to generate the permutations of a list.
'''


def permute(L):
    yield L
    stack = [(0, i) for i in range(len(L) - 1, 0, -1)]
    while stack:
        low, high = stack.pop()
        if high % 2:
            L[low], L[high] = L[high], L[low]
        else:
            L[0], L[high] = L[high], L[0]
        yield L
        if low + 1 != high:
            stack.append((low + 1, high))
        for i in range(high - 1, 0, -1):
            stack.append((0, i))

