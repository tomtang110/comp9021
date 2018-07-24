# Written by Eric Martin for COMP9021


'''
Describes all sets of positive integers {x, y, z} such that x, y and z have no occurrence of 0,
every nonzero digit occurs exactly once in one of x, y or z, and x, y and z are perfect squares.

Extracts digits by converting numbers to sets of characters.
'''


from math import sqrt
    

def digits_if_ok(number, digits_seen_before):
    number_str = str(number)
    digits_seen_now = digits_seen_before | set(number_str)
    if len(digits_seen_now) != len(digits_seen_before) + len(number_str):
        return
    return digits_seen_now


# If it was a perfect square, max_square would, associated with 1 and 4,
# be the largest member of a possible solution.
max_square = 9876532
nb_of_solutions = 0
upper_bound = round(sqrt(max_square)) + 1
set_of_all_digits = {str(i) for i in range(10)}
for x in range(1, upper_bound):
    x_square = x * x
    # digits_in_x_square_and_0 is not None
    # iff all digits in x_square are distinct and not equal to 0.
    digits_in_x_square_and_0 = digits_if_ok(x_square, {'0'})
    if not digits_in_x_square_and_0:
        continue
    for y in range(x + 1, upper_bound):
        y_square = y * y
        # digits_in_x_square_and_y_square_and_0 is not None
        # iff all digits in y_square are distinct, distinct to 0,
        # and distinct to all digits in x_square.
        digits_in_x_square_and_y_square_and_0 = digits_if_ok(y_square, digits_in_x_square_and_0)
        if not digits_in_x_square_and_y_square_and_0:
            continue
        for z in range(y + 1, upper_bound):
            z_square = z * z
            # digits_in_x_square_and_y_square_and_z_square_and_0 is not None
            # iff all digits in z_square are distinct, distinct to 0,
            # and distinct to all digits in x_square and y_square.
            digits_in_x_square_and_y_square_and_z_square_and_0 =\
                                       digits_if_ok(z_square, digits_in_x_square_and_y_square_and_0)
            if not digits_in_x_square_and_y_square_and_z_square_and_0:
                continue
            if digits_in_x_square_and_y_square_and_z_square_and_0 != set_of_all_digits:
                continue
            print(f'{x_square:7d} {y_square:7d} {z_square:7d}')
            nb_of_solutions += 1
print(f'\nAltogether, {nb_of_solutions} solutions have been found.')

