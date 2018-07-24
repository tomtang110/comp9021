# Written by Eric Martin for COMP9021


from math import sqrt


def is_prime(N):
    '''Returns True or False depending on whether
    the number provided as argument is prime or not, respectively.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(99793)
    True
    >>> is_prime(99967)
    False
    '''
    if N == 2:
        return True
    if N < 2 or N % 2 == 0:
        return False 
    # We let primes_sieve encode the sequence (2, 3, 5, 7, 9, 11, ..., N')
    # with N' equal to N if N is odd and N - 1 is N is even.
    # The index of N' is N_index
    N_index = (N - 1) // 2
    primes_sieve = [True] * (N_index + 1)
    for n in range(1, (round(sqrt(N)) + 1) // 2):
        if primes_sieve[n]:
            if N % (2 * n + 1) == 0:
                return False
            # If n is the index of p then
            # 2 * n * (n + 1) is the index of p ** 2;
            # Also, we increment the value by 2p,
            # which corresponds to increasing the index by 2 * n + 1.
            for i in range(2 * n * (n + 1), N_index + 1, 2 * n + 1):
                primes_sieve[i] = False
    return True


def list_of_primes_up_to(N):
    '''Generates the list of all prime numbers at most equal
    to the number provided as argument.

    >>> list_of_primes_up_to(1)
    []
    >>> list_of_primes_up_to(2)
    [2]
    >>> list_of_primes_up_to(10)
    [2, 3, 5, 7]
    >>> list_of_primes_up_to(11)
    [2, 3, 5, 7, 11]
    >>> list_of_primes_up_to(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    '''
    if N < 2:
        return []
    # We let primes_sieve encode the sequence (2, 3, 5, 7, 9, 11, ..., N')
    # with N' equal to N if N is odd and N - 1 is N is even.
    # The index of N' is N_index
    N_index = (N - 1) // 2
    primes_sieve = [True] * (N_index + 1)
    for n in range(1, (round(sqrt(N)) + 1) // 2):
        if primes_sieve[n]:
            # If n is the index of p then
            # 2 * n * (n + 1) is the index of p ** 2;
            # Also, we increment the value by 2p,
            # which corresponds to increasing the index by 2 * n + 1.
            for i in range(2 * n * (n + 1), N_index + 1, 2 * n + 1):
                primes_sieve[i] = False
    list_of_primes = [2]
    for n in range(1, N_index + 1):
        if primes_sieve[n]:
            list_of_primes.append(2 * n + 1)
    return list_of_primes


def generate_next_prime():
    '''A generator to provide prime numbers one by one
    in sequence on demand.
    
    >>> primes = generate_next_prime()
    >>> next(primes)
    2
    >>> next(primes)
    3
    >>> next(primes)
    5
    >>> next(primes)
    7
    >>> next(primes)
    11
    '''
    yield 2
    yield 3
    yield 5
    primes = [5]
    add_two = True
    prime_candidate = 5
    while True:
        # We skip multiples of 2 and multiples of 3,
        # noting that every third odd number is a multiple of 3,
        # and all other multiples of 3 are multiples of 2.
        if add_two:
            prime_candidate += 2
        else:
            prime_candidate += 4
        add_two = not add_two
        j = 0
        while primes[j] * primes[j] <= prime_candidate:
            if prime_candidate % primes[j] == 0:
                break
            j += 1
        else:
            primes.append(prime_candidate)
            yield prime_candidate


def prime_decomposition(N):
    '''Generates a list consisting of pairs of the form
    (p, k) with p a prime number and k >=1 if
    the prime decomposition of the number provided as argument
    contains k times p, except for the special cases where
    that number is 0 or 1.
    
    >>> prime_decomposition(0)
    [(0, 1)]
    >>> prime_decomposition(1)
    [(1, 1)]
    >>> prime_decomposition(2)
    [(2, 1)]
    >>> prime_decomposition(4)
    [(2, 2)]
    >>> prime_decomposition(10)
    [(2, 1), (5, 1)]
    >>> prime_decomposition(12345)
    [(3, 1), (5, 1), (823, 1)]
    >>> prime_decomposition(10000)
    [(2, 4), (5, 4)]
    >>> prime_decomposition(121212)
    [(2, 2), (3, 2), (7, 1), (13, 1), (37, 1)]
    '''
    list_of_primes = list_of_primes_up_to(N // 2)
    decomposition = []
    for p in list_of_primes:
        if N % p == 0:
            exp = 1
            while N % p ** (exp + 1) == 0:
                exp += 1
            decomposition.append((p, exp))
    if not decomposition:
        return [(N, 1)]
    return decomposition


def prime_decompositions_up_to(N):
    '''Generates a list of lengh 1 + the number provided as argument
    whose elements are dictionaries and such that for all numbers
    N at most equal to the number provided as argument, the dictionary
    at index N has a key p and an associated value k with p a prime number
    and k >=1 if the prime decomposition of N contains k times p,
    except for the special cases where N is 0 or 1.
    
    >>> prime_decompositions_up_to(0)
    [{0: 1}]
    >>> prime_decompositions_up_to(1)
    [{0: 1}, {1: 1}]
    >>> prime_decompositions_up_to(2)
    [{0: 1}, {1: 1}, {2: 1}]
    >>> prime_decompositions_up_to(3)
    [{0: 1}, {1: 1}, {2: 1}, {3: 1}]
    >>> prime_decompositions_up_to(7)
    [{0: 1}, {1: 1}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}]
    '''
    decompositions = [{0: 1}, {1: 1}] + [None] * (N - 1)
    for i in range(2, N + 1):
        decompositions[i] = {}
    for n in range(2, N + 1):
        if not decompositions[n]:
            # Then n is a prime number.
            exp = 1
            power_of_n = n ** exp
            while power_of_n <= N:
                for i in range(power_of_n, N + 1, power_of_n):
                    decompositions[i][n] = exp
                exp += 1
                power_of_n = n ** exp
    return decompositions[: N + 1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
