# Written by Eric Martin for COMP9021


'''
Computes the hash code of a string as a 32 bit number
that aggregates the ascii codes of all characters in the string,
at each step shifting the resulting code by a given number.
'''


from collections import defaultdict


def hash_code(word, shift):
    mask = (1 << 32) - 1
    code = 0
    for c in word:       
        code = (code << shift & mask) | (code >> 32 - shift)       
        code += ord(c)
    return code

def hash_all_words(shift):
    words_file = open('words.txt')
    codes = defaultdict(int)
    for word in words_file:
        codes[hash_code(word[: -1], shift)] += 1
    return sorted(list(codes.values()), reverse = True)

def find_best_shifts(top_shifts, bottom_hashes):
    hash_counts_per_shift = []
    for shift in range(32):
        hash_counts = hash_all_words(shift)
        hash_counts_per_shift.append((hash_counts[: bottom_hashes], shift))
    return sorted(hash_counts_per_shift)[: top_shifts]


if __name__ == '__main__':
    print('Bottom 4 hashes for shift of 0:')
    print(hash_all_words(0)[: 4])
    print('\nBest 6 shifts for bottom 4 hashes:')
    best_shifts = find_best_shifts(6, 4)
    for hashes, shift in best_shifts:
        print(f'{shift:2d} : {hashes}')
        
        
        
            
           

