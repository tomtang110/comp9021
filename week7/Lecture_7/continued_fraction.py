# Written by Eric Martin for COMP9021


'''
A class for fractions and a class for continued fractions,
to approximate fractions to decimals with an arbitrary precision,
and to approximate continued fractions, so square roots in particular,
to fractions and decimals with an arbitrary precision.
'''


import math
from itertools import cycle, chain


class ContinuedFractionError(Exception):
    def __init__(self, message):
        self.message = message

        
class ContinuedFraction:
    '''
    If the continued fraction is finite, then we make sure it does not end in 1.
    Otherwise, periodic_expansion is made nonperiodic, and as much from finite_expansion is removed.
 
    >>> print(ContinuedFraction())
    [0]
    >>> print(ContinuedFraction([0, 1]))
    [1]
    >>> print(ContinuedFraction([1, 2, 1]))
    [1, 3]
    >>> print(ContinuedFraction([0, 1], [1]))
    [0; 1...]
    >>> print(ContinuedFraction([0], [1, 2, 1, 2, 1, 2]))
    [0; 1, 2...]
    >>> print(ContinuedFraction([0, 2], [1, 2, 1, 2, 1, 2]))
    [0; 2, 1...]
    >>> print(ContinuedFraction([0, 1, 2, 3], [4, 2, 3, 4, 2, 3]))
    [0, 1; 2, 3, 4...]
    >>> print(ContinuedFraction([0, 1, 2, 3, 1], [4, 2, 3, 1]))
    [0, 1; 2, 3, 1, 4...]
    '''
    def __init__(self, finite_expansion = None, periodic_expansion = None):
        if finite_expansion is not None and (not isinstance(finite_expansion, list) or
                                            any(not isinstance(e, int) for e in finite_expansion) or
                                                          any(e <= 0 for e in finite_expansion[1: ])
                                            ):
            raise ContinuedFractionError('Incorrect finite expansion')
        if periodic_expansion is not None and (not isinstance(periodic_expansion, list) or
                                          any(not isinstance(e, int) for e in periodic_expansion) or
                                                             any(e <= 0 for e in periodic_expansion)
                                             ):
            raise ContinuedFractionError('Incorrect periodic expansion')
        if finite_expansion:
            self.finite_expansion = finite_expansion
        else:
            self.finite_expansion = [0]
        if periodic_expansion:
            self.periodic_expansion = periodic_expansion
        else:
            self.periodic_expansion = []
        self._normalise()

    def _normalise(self):
        if self.periodic_expansion:
            for i in range(2, len(self.periodic_expansion) // 2 + 1):
                if len(self.periodic_expansion) % i == 0 and self.periodic_expansion ==\
                                 self.periodic_expansion[: i] * (len(self.periodic_expansion) // i):
                    self.periodic_expansion = self.periodic_expansion[: i]
                    break
            while len(self.finite_expansion) > 1 and self.finite_expansion[-1] and\
                                           self.finite_expansion[-1] == self.periodic_expansion[-1]:
                    self.finite_expansion.pop()
                    self.periodic_expansion = [self.periodic_expansion[-1]] +\
                                                                       self.periodic_expansion[: -1]
        elif len(self.finite_expansion) > 1 and self.finite_expansion[-1] == 1:
            self.finite_expansion.pop()
            self.finite_expansion[-1] += 1
        
    def is_integral(self):
        return len(self.finite_expansion) == 1 and not self.periodic_expansion

    def is_rational(self):
        return not self.periodic_expansion

    def negation(self):
        '''
        >>> print(ContinuedFraction().negation())
        [0]
        >>> print(ContinuedFraction([1]).negation())
        [-1]
        >>> print(ContinuedFraction([-1]).negation())
        [1]
        >>> print(ContinuedFraction([0, 1]).negation())
        [-1]
        >>> print(ContinuedFraction([1, 2]).negation())
        [-2, 2]
        >>> print(ContinuedFraction([-2, 2]).negation())
        [1, 2]
        >>> print(ContinuedFraction([1, 3]).negation())
        [-2, 1, 2]
        >>> print(ContinuedFraction([-2, 1, 2]).negation())
        [1, 3]
        >>> print(ContinuedFraction([1, 3, 4], [5, 6]).negation())
        [-2, 1, 2, 4; 5, 6...]
        >>> print(ContinuedFraction([-2, 1, 2, 4], [5, 6]).negation())
        [1, 3, 4; 5, 6...]
        '''
        # In case the periodic expansion is not empty, borrow from it so as to make
        # the length of the finite expansion at least 3, as that simplifies the computation.
        if len(self.periodic_expansion) == 1:
            finite_expansion = self.finite_expansion + self.periodic_expansion * 2
        elif self.periodic_expansion:
            finite_expansion = self.finite_expansion + self.periodic_expansion
        else:
            finite_expansion = self.finite_expansion           
        periodic_expansion = self.periodic_expansion            
        if len(finite_expansion) == 1:
            return ContinuedFraction([-finite_expansion[0]])
        # In this case, finite_expansion is of length at least 3.
        if finite_expansion[1] == 1:
            return ContinuedFraction([-finite_expansion[0] - 1, 1 + finite_expansion[2]] +
                                                           finite_expansion[3: ], periodic_expansion
                                    )
        return ContinuedFraction([-finite_expansion[0] - 1, 1, finite_expansion[1] - 1] +
                                                           finite_expansion[2: ], periodic_expansion
                                )

    def to_fraction(self):
        '''
        >>> print(ContinuedFraction().to_fraction())
        0 / 1
        >>> print(ContinuedFraction([0, 1]).to_fraction())
        1 / 1
        >>> print(ContinuedFraction([0, 2]).to_fraction())
        1 / 2
        >>> print(ContinuedFraction([0, 1, 1]).to_fraction())
        1 / 2
        >>> print(ContinuedFraction([2, 1, 4, 3]).to_fraction())
        45 / 16
        >>> print(ContinuedFraction([2, 1, 4, 2, 1]).to_fraction())
        45 / 16
        '''
        if not self.is_rational():
            return
        p1, p2 = 0, 1
        q1, q2 = 1, 0
        for e in self.finite_expansion:
            p1, p2 = p2, e * p2 + p1
            q1, q2 = q2, e * q2 + q1
        return Fraction(p2, q2)

    def approximate_as_fractions(self):
        '''
        >>> for f in ContinuedFraction([0]).approximate_as_fractions(): print(f)
        0 / 1
        >>> for f in ContinuedFraction([0, 2]).approximate_as_fractions(): print(f)
        0 / 1
        1 / 2
        >>> cf = ContinuedFraction([1], [2]) # sqrt(2)
        >>> fractions = cf.approximate_as_fractions()
        >>> for _ in range(10): print(next(fractions))
        1 / 1
        3 / 2
        7 / 5
        17 / 12
        41 / 29
        99 / 70
        239 / 169
        577 / 408
        1393 / 985
        3363 / 2378
        >>> cf = ContinuedFraction([-2, 3], [1, 2]) # -sqrt(3)
        >>> fractions = cf.approximate_as_fractions()
        >>> for _ in range(10): print(next(fractions))
        -2 / 1
        -5 / 3
        -7 / 4
        -19 / 11
        -26 / 15
        -71 / 41
        -97 / 56
        -265 / 153
        -362 / 209
        -989 / 571
        '''
        p1, p2 = 0, 1
        q1, q2 = 1, 0
        for e in chain(self.finite_expansion, cycle(self.periodic_expansion)):
            p1, p2 = p2, e * p2 + p1
            q1, q2 = q2, e * q2 + q1
            yield Fraction(p2, q2)

    def approximate_as_decimals(self, precision = 0):
        '''
        >>> cf = ContinuedFraction()
        >>> decimals = cf.approximate_as_decimals()
        >>> for _ in range(3): print(next(decimals))
        0.
        0.
        0.
        >>> f = cf = ContinuedFraction([2])
        >>> decimals = cf.approximate_as_decimals()
        >>> for _ in range(3): print(next(decimals))
        2.
        2.
        2.
        >>> cf = ContinuedFraction([0, 2])
        >>> decimals = cf.approximate_as_decimals()
        >>> for _ in range(3): print(next(decimals))
        0.
        0.5
        0.5
        >>> cf = ContinuedFraction([0, 3])
        >>> decimals = cf.approximate_as_decimals(4)
        >>> for _ in range(5): print(next(decimals))
        0.3333
        0.33333333
        0.333333333333
        0.3333333333333333
        0.33333333333333333333
        >>> cf = ContinuedFraction([-1, 1, 2])
        >>> decimals = cf.approximate_as_decimals(4)
        >>> for _ in range(5): print(next(decimals))
        -0.3333
        -0.33333333
        -0.333333333333
        -0.3333333333333333
        -0.33333333333333333333
        >>> cf = ContinuedFraction([1], [2]) # sqrt(2)
        >>> decimals = cf.approximate_as_decimals()
        >>> for _ in range(10): print(next(decimals))
        1.
        1.4
        1.41
        1.414
        1.4142
        1.41421
        1.414213
        1.4142135
        1.41421356
        1.414213562
        >>> cf = ContinuedFraction([-2, 3], [1, 2]) # -sqrt(3)
        >>> decimals = cf.approximate_as_decimals(2)
        >>> for _ in range(10): print(next(decimals))
        -1.73
        -1.7320
        -1.732050
        -1.73205080
        -1.7320508075
        -1.732050807568
        -1.73205080756887
        -1.7320508075688772
        -1.732050807568877293
        -1.73205080756887729352
        '''
        if self.is_rational():
            yield from self.to_fraction().approximate_as_decimals(precision)
        else:
            current_precision = precision
            if self.finite_expansion[0] >= 0 or self.is_integral():
                integral_part = str(self.finite_expansion[0]) + '.'
            else:
                integral_part = str(self.finite_expansion[0] + 1) + '.'          
            fractions = self.approximate_as_fractions()
            next(fractions)
            while True:
                yield integral_part + ''.join(str(digit) for digit in
                                         self._approximate_as_decimals(fractions, current_precision)
                                             )
                current_precision += max(precision, 1)

    def _approximate_as_decimals(self, fractions, precision):
        fraction = next(fractions)
        s1 = fraction._get_precision_many_decimals(abs(fraction.numerator) %
                                          fraction.denominator * 10, fraction.denominator, precision
                                                  )
        while True:
            fraction = next(fractions)
            s2 = fraction._get_precision_many_decimals(abs(fraction.numerator) % 
                                          fraction.denominator * 10, fraction.denominator, precision
                                                      )
            if s1 == s2:
                break
            s1 = s2
        return s1

    def __str__(self):
        string = str(self.finite_expansion)
        if self.periodic_expansion:
            string = string[: -1] + '; ' + str(self.periodic_expansion)[1: -1] + '...]'
        return string
    

class FractionError(Exception):
    def __init__(self, message):
        self.message = message


class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        if not isinstance(numerator, int):
            raise FractionError('Incorrect numerator')
        if not isinstance(denominator, int):
            raise FractionError('Incorrect denominator')            
        gcd = math.gcd(numerator, denominator)
        if numerator * denominator >= 0:
            self.numerator = abs(numerator) // gcd
        else:
            self.numerator = -abs(numerator) // gcd
        self.denominator = abs(denominator) // gcd

    def to_continued_fraction(self):
        '''
        >>> print(Fraction().to_continued_fraction())
        [0]
        >>> print(Fraction(2).to_continued_fraction())
        [2]
        >>> print(Fraction(-2).to_continued_fraction())
        [-2]
        >>> print(Fraction(1, 2).to_continued_fraction())
        [0, 2]
        >>> print(Fraction(1, -2).to_continued_fraction())
        [-1, 2]
        >>> print(Fraction(8, 5).to_continued_fraction())
        [1, 1, 1, 2]
        >>> print(Fraction(-8, 5).to_continued_fraction())
        [-2, 2, 2]
        >>> print(Fraction(15, 11).to_continued_fraction())
        [1, 2, 1, 3]
        >>> print(Fraction(-1080, -384).to_continued_fraction())
        [2, 1, 4, 3]
        '''
        factors = []
        a, b = abs(self.numerator), self.denominator
        while b:
            factors.append(a // b)
            a, b = b, a % b
        if self.numerator >= 0:
            return ContinuedFraction(factors)
        return ContinuedFraction(factors).negation()
        

    def approximate_as_decimals(self, precision = 0):
        '''
        >>> f = Fraction()
        >>> decimals = f.approximate_as_decimals()
        >>> for _ in range(3): print(next(decimals))
        0.
        0.
        0.
        >>> f = Fraction(2)
        >>> decimals = f.approximate_as_decimals()
        >>> for _ in range(3): print(next(decimals))
        2.
        2.
        2.
        >>> f = Fraction(-2)
        >>> decimals = f.approximate_as_decimals()
        >>> for _ in range(3): print(next(decimals))
        -2.
        -2.
        -2.
        >>> f = Fraction(1, 2)
        >>> decimals = f.approximate_as_decimals()
        >>> for _ in range(3): print(next(decimals))
        0.
        0.5
        0.5
        >>> f = Fraction(1, 3)
        >>> decimals = f.approximate_as_decimals(4)
        >>> for _ in range(5): print(next(decimals))
        0.3333
        0.33333333
        0.333333333333
        0.3333333333333333
        0.33333333333333333333
        >>> f = Fraction(7, 3)
        >>> decimals = f.approximate_as_decimals(4)
        >>> for _ in range(5): print(next(decimals))
        2.3333
        2.33333333
        2.333333333333
        2.3333333333333333
        2.33333333333333333333
        >>> f = Fraction(-1, 3)
        >>> decimals = f.approximate_as_decimals(4)
        >>> for _ in range(5): print(next(decimals))
        -0.3333
        -0.33333333
        -0.333333333333
        -0.3333333333333333
        -0.33333333333333333333
        >>> f = Fraction(-7, 3)
        >>> decimals = f.approximate_as_decimals(4)
        >>> for _ in range(5): print(next(decimals))
        -2.3333
        -2.33333333
        -2.333333333333
        -2.3333333333333333
        -2.33333333333333333333
        '''
        if self.numerator >= 0 or self.denominator == 1:
            integral_part = str(self.numerator // self.denominator)
        else:
            integral_part = '-' + str(abs(self.numerator) // self.denominator)
        current_precision = precision
        while True:
            yield ''.join((integral_part, '.', ''.join(str(digit) for digit in
                                                                  self._get_precision_many_decimals(
                                      abs(self.numerator) % self.denominator * 10, self.denominator,
                                                                                   current_precision
                                                                                                   )
                                                      )
                          )
                         )
            current_precision += max(precision, 1)

    def _get_precision_many_decimals(self, p, q, precision):
        decimals = []
        for _ in range(precision):
            if not p:
                return decimals
            decimals.append(p // q)
            p = p % q * 10
        return decimals

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
