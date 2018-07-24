def hanoi(n,A,B,C):
    if n == 1:
        print(f'Move disk from {A} to {C}')
    else:
        hanoi(n-1,A,C,B)
        print(f'Move disk from {A} to {C}')
        hanoi(n-1,B,A,C)
        
