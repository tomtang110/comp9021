# Written by Eric Martin for COMP9021


'''
Utility to prompt the user for an integer with a range that can be specified,
until the user input is of the expected type.
'''


def input_int(prompt = 'What do you want N to be? ', min_value = float('-inf'),
                                                                            max_value = float('inf')
             ):
    while True:
        try:
            input_value = int(input(prompt))
            if input_value < min_value or input_value > max_value:
                raise ValueError
            return input_value
        except ValueError:
            print('Incorrect input. ', end = '')
