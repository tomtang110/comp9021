# Written by Eric Martin for COMP9021


'''
Computes the (n+1)st Fibonacci number iteratively and recursively,
with and without memoisation.
'''


def iterative_fibonacci(n):
    if n < 2:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

def recursive_fibonacci(n):
    if n >= 2:
        return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)
    return n

def memoise_fibonacci(n, fibonacci = {0: 0, 1: 1}):
    if n not in fibonacci:
        fibonacci[n] = memoise_fibonacci(n - 1) + memoise_fibonacci(n - 2)
    return fibonacci[n]


if __name__ == '__main__':
    print('Generating the first 40 nonzero Fibonacci numbers:')
    for n in range(1, 41):
        print(iterative_fibonacci(n), end = ' ')
        if n % 10 == 0:
            print()
    print()
    print('Generating the first 40 nonzero Fibonacci numbers recursively '
          'up to 40, with memoisation:')
    for n in range(1, 41):
        print(memoise_fibonacci(n), end = ' ')
        if n % 10 == 0:
            print()
    print()
    print('Generating the first 40 nonzero Fibonacci numbers recursively '
          'up to 40, without memoisation:')
    for n in range(1, 41):
        print(recursive_fibonacci(n), end = ' ')
        if n % 10 == 0:
            print()

