from math import ceil,sqrt
from random import randint
height = int(input('building height:'))
max_nb =ceil((-1+sqrt(1+8*height))/2)
print('max drop is ', max_nb)
break_floor=randint(1,height+1)
min_floor=0
max_floor=height + 1
nb_of_drops_left = max_nb
jump = max_nb
marble_nb=1
while max_floor - min_floor >1:
    floor_to_go = min_floor + jump
    print(f'Dropping from floor {floor_to_go}')
    if floor_to_go >= break_floor:
        print(f'Marble nb {marble_nb} breaks')
        marble_nb = 2
        jump =1
        max_floor =floor_to_go
    else:
        print(f'Marble nb {marble_nb} does not breaks')
        if marble_nb == 1:
            jump -= 1
        min_floor = floor_to_go
