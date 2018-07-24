# Written by Eric Martin for COMP9021


'''
Represents a second-order equation as a class with a, b, c, root_1 and root_2 as data.
By default, a is set to 1 and b and c are set to 0.
The parameters can be changed with the update_parameters() function.
Whether the parameters are changed when the equation is created or by a call to
the update_parameters() function, a, b and c have to be explictly named.
The roots are automatically computed when the equation is created or when
some parameter is updated.
'''


from math import sqrt


class SecondOrderEquationError(Exception):
    def __init__(self, message):
        self.message = message


class SecondOrderEquation:
    '''
    >>> eq = SecondOrderEquation(a = 0, b = 1)
    Traceback (most recent call last):
    ...
    SecondOrderEquationError: a cannot be equal to 0.
    >>> eq = SecondOrderEquation()
    >>> eq.a
    1
    >>> eq.b
    0
    >>> eq.c
    0
    >>> eq.root_1
    0.0
    >>> eq.root_2
    0.0
    >>> eq = SecondOrderEquation(b = 4)
    >>> eq.root_1
    -4.0
    >>> eq.root_2
    0.0
    >>> eq = SecondOrderEquation(a = 1, b = 3, c = 2)
    >>> eq.root_1
    -2.0
    >>> eq.root_2
    -1.0
    >>> eq.update_parameters(a = 0)
    Traceback (most recent call last):
    ...
    SecondOrderEquationError: a cannot be equal to 0.
    >>> eq.update_parameters(b = -1)
    >>> eq.root_1
    >>> eq.root_2
    >>> eq.update_parameters(c = 0.3, a = 0.5)
    >>> eq.root_1
    0.3675444679663241
    >>> eq.root_2
    1.632455532033676
    '''
    def __init__(self, *, a = 1, b = 0, c = 0):
        if a == 0:
            raise SecondOrderEquationError('a cannot be equal to 0.')
        self.a = a
        self.b = b
        self.c = c
        self._compute_delta()
        self._compute_roots()

    def __repr__(self):
        '''
        >>> SecondOrderEquation()
        SecondOrderEquation(a = 1, b = 0, c = 0)
        >>> SecondOrderEquation(c = -5, a = 2)
        SecondOrderEquation(a = 2, b = 0, c = -5)
        >>> SecondOrderEquation(b = 1, a = -1, c = -1)
        SecondOrderEquation(a = -1, b = 1, c = -1)
        '''
        return f'SecondOrderEquation(a = {self.a}, b = {self.b}, c = {self.c})'

    def __str__(self):
        '''
        >>> print(SecondOrderEquation())
        x^2 = 0
        >>> print(SecondOrderEquation(c = -5, a = 2))
        2x^2 - 5 = 0
        >>> print(SecondOrderEquation(b = 1, a = -1, c = -1))
        -x^2 + x - 1 = 0
        '''
        if self.a == 1:
            equation = 'x^2'
        elif self.a == -1:
            equation = '-x^2'
        else:
            equation = f'{self.a}x^2'
        if self.b == 1:
            equation += ' + x'
        elif self.b == -1:
            equation -= ' - x'           
        elif self.b > 0:
            equation += f' + {self.b}x'
        elif self.b < 0:
            equation += f'- {-self.b}x'
        if self.c > 0:
            equation += f' + {self.c}'
        elif self.c < 0:
            equation += f' - {-self.c}'
        return f'{equation} = 0'

    def _compute_delta(self):
        self.delta = self.b * self.b - 4 * self.a * self.c

    def _compute_roots(self):
        if self.delta < 0:
            self.root_1 = self.root_2 = None
        elif self.delta == 0:
            self.root_1 = self.root_2 = -self.b / (2 * self.a)
        else:
            sqrt_delta = sqrt(self.delta)
            self.root_1 = (-self.b - sqrt_delta) / (2 * self.a)
            self.root_2 = (-self.b + sqrt_delta) / (2 * self.a)

    def update_parameters(self, *, a = None, b = None, c = None):
        if a == 0:
            raise SecondOrderEquationError('a cannot be equal to 0.')
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if c is not None:
            self.c = c
        self._compute_delta()
        self._compute_roots()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
        


        
