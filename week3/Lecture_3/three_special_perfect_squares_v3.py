# Written by Eric Martin for COMP9021


'''
Describes all sets of positive integers {x, y, z} such that x, y and z have no occurrence of 0,
every nonzero digit occurs exactly once in one of x, y or z, and x, y and z are perfect squares.

Extracts digits using the % and // operators and encodes them as a natural number.
'''


from math import sqrt
    

def encoding_if_ok(number, encoded_number):
    while number:
        # Extract rightmost digit, d, from number
        digit = number % 10
        # Check that that d is not encoded in encoded_number
        if 1 << digit & encoded_number:
            return
        # Add encoding of d to encoded_number
        encoded_number |= 1 << digit
        # Get rid of d in number
        number //= 10
    return encoded_number


# If it was a perfect square, max_square would, associated with 1 and 4,
# be the largest member of a possible solution. */
max_square = 9876532
nb_of_solutions = 0
upper_bound = round(sqrt(max_square)) + 1
encoding_of_all_digits = 2 ** 10 - 1
for x in range(1, upper_bound):
    x_square = x * x
    # encoded_0_and_x_square is not None
    # iff all digits in x_square are distinct and not equal to 0
    # (encoded as 1)
    encoded_0_and_x_square = encoding_if_ok(x_square, 1)
    if not encoded_0_and_x_square:
        continue
    for y in range(x + 1, upper_bound):
        y_square = y * y
        # encoded_0_and_x_square_and_y_square is not None
        # iff all digits in y_square are distinct, distinct to 0,
        # and distinct to all digits in x_square
        encoded_0_and_x_square_and_y_square = encoding_if_ok(y_square, encoded_0_and_x_square)
        if not encoded_0_and_x_square_and_y_square:
            continue
        for z in range(y + 1, upper_bound):
            z_square = z * z
            # encoded_0_and_x_square_and_y_square_and_z_square is not None
            # iff all digits in z_square are distinct, distinct to 0,
            # and distinct to all digits in x_square and y_square
            encoded_0_and_x_square_and_y_square_and_z_square =\
                  encoding_if_ok(z_square, encoded_0_and_x_square_and_y_square)
            if not encoded_0_and_x_square_and_y_square_and_z_square:
                continue
            if encoded_0_and_x_square_and_y_square_and_z_square != encoding_of_all_digits:
                continue
            print(f'{x_square:7d} {y_square:7d} {z_square:7d}')
            nb_of_solutions += 1
print(f'\nAltogether, {nb_of_solutions} solutions have been found.')

