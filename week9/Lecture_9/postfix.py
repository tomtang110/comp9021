# Written by Eric Martin for COMP9021


'''
Uses the Stack interface to evaluate an arithmetic expression written in postfix
and built from natural numbers using the binary +, -, * and / operators.             
'''


import re
from operator import add, sub, mul, truediv

from stack_adt import Stack, EmptyStackError


def evaluate(expression):
    '''
    Checks whether an expression is a valid postfix expression,
    and in case the answer is yes, returns the value of the expression,
    provided that no division by 0 is attempted; otherwise, return None.

    >>> evaluate('12')
    12
    >>> evaluate('12 345 +')
    357
    >>> evaluate('1 2 3 4 5 6 + - + - +')
    7
    >>> evaluate('10 2 * 30 4 * -')
    -100
    >>> evaluate('12 13 4 5+ + 10 -  7 8 * /+')
    12.214285714285714
    >>> evaluate('2 +')
    >>> evaluate('2 3')
    >>> evaluate('2 / 3')
    >>> evaluate('2 0 /')
    '''
    if any(not (c.isdigit() or c.isspace() or c in '+-*/') for c in expression):
        return
    # Tokens can be natural numbers, +, -, *, and /
    tokens = re.compile('(\d+|\+|-|\*|/)').findall(expression)
    try:
        value = evaluate_expression(tokens)
        return value
    except ZeroDivisionError:
        return

def evaluate_expression(tokens):
    stack = Stack()
    for token in tokens:
        try:
            token = int(token)
            stack.push(token)
        except ValueError:
            try:
                arg_2 = stack.pop()
                arg_1 = stack.pop()
                stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[token](arg_1, arg_2))
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
