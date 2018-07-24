# Written by Eric Martin for COMP9021


'''
Generates an initial segment of the list of prime numbers based on Euler sieve
switching between sets and sorted lists for a more effective implementation.
'''


from math import sqrt

from input_int import input_int


def generate_primes():
    print('I will generate all prime numbers in the range [2, N].')
    N = input_int()
    if N < 2:
        return
    primes(N)

def primes(N):
    primes_sieve_list = range(2, N + 1)
    i = 0
    while primes_sieve_list[i] <= round(sqrt(N)):
        primes_sieve_set = set(primes_sieve_list)
        k = 0
        while True:
            factor = primes_sieve_list[i] * primes_sieve_list[i + k]
            if factor > N:
                break
            primes_sieve_set.remove(factor)
            k += 1
        primes_sieve_list = sorted(primes_sieve_set)
        i += 1

    field_width = len(str(N)) + 2
    nb_of_fields = 60 // field_width
    for (count, n) in enumerate(primes_sieve_list, 1):
        print(f'{n:{field_width}d}', end = '')
        if count % nb_of_fields == 0:
            print()
    if count % nb_of_fields:
        print()


if __name__ == '__main__':
    generate_primes()
