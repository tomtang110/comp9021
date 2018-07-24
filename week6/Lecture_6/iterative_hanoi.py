# Written by Eric Martin for COMP9021


'''
Iterative solution to the towers of Hanoi puzzle.
'''


def move_towers(n, start_position, end_position, intermediate_position):
    '''
    Move a tower of n disks from start_position to end_position,
    with intermediate_position available.
    '''
    smallest_disk_position = 0
    direction = 1 - n % 2 * 2
    stacks = list(range(n, 0, -1)), [], []
    for i in range(2 ** n - 1):
        if i % 2 == 0:
            new_smallest_disk_position = (smallest_disk_position + direction) % 3
            print(f'Move smallest disk from {smallest_disk_position} to '
                                                                    f'{new_smallest_disk_position}'
                 )
            stacks[new_smallest_disk_position].append(stacks[smallest_disk_position].pop())
            smallest_disk_position = new_smallest_disk_position
        else:
            other_positions = (smallest_disk_position + 1) % 3, (smallest_disk_position + 2) % 3
            if not stacks[other_positions[0]]:
                from_position, to_position = other_positions[1], other_positions[0]
            elif not stacks[other_positions[1]]:
                from_position, to_position = other_positions[0], other_positions[1]
            elif stacks[other_positions[0]][-1] < stacks[other_positions[1]][-1]:
                from_position, to_position = other_positions[0], other_positions[1]
            else:
                from_position, to_position = other_positions[1], other_positions[0]
            stacks[to_position].append(stacks[from_position].pop())
            print(f'Move disk of size {stacks[to_position][-1]} from {from_position} to '
                                                                                   f'{to_position}'
                 )

            
move_towers(4, 0, 2, 1)
