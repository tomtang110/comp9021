# Written by Eric Martin for COMP9021


'''
Recursive solution to the Tower of Hanoi puzzle.
'''


def move_towers(n, start_position, end_position, intermediate_position):
    '''
    Move a tower of n disks from start_position to end_position,
    with intermediate_position available.
    '''
    if n == 1:
        print(f'Move smallest disk from {start_position} to {end_position}')
    else:
        move_towers(n - 1, start_position, intermediate_position, end_position)
        print(f'Move disk of size {n} from {start_position} to {end_position}')
        move_towers(n - 1, intermediate_position, end_position, start_position)


move_towers(4, 0, 2, 1)
