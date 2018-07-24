# Written by Eric Martin for COMP9021


'''
Separate chaining of compressed hash_codes
'''


from cyclic_shift_hash import hash_code


class HashTable:
    def __init__(self, capacity =  65537):
        self._capacity = capacity
        self._table = [set() for _ in range(capacity)]
        self._cycle = 6
        self._size = 0

    def _compressed_hash_code(self, word):
        return hash_code(word, self._cycle) % self._capacity

    def __len__(self):
        return self._size

    def add_word(self, word):
        self._table[self._compressed_hash_code(word)].add(word)
        self._size += 1

    def find_word(self, word):
        code = self._compressed_hash_code(word)
        return word in self._table[code]

    def delete_word(self, word):
        code = self._compressed_hash_code(word)
        if not self._table[code]:
            return False
        if word in self._table[code]:
            self._table[code].remove(word)
            self._size -= 1
            return True
        return False


if __name__ == '__main__':
    hash_table = HashTable()
    words_file = open('words.txt')
    for word in words_file:
        hash_table.add_word(word[: -1])
    bucket_sizes = [len(hash_table._table[i]) for i in range(hash_table._capacity)
                                                                             if hash_table._table[i]
                   ]
    bucket_sizes.sort(reverse = True)
    print('Nb of words: ', len(hash_table))
    print('Nb of compressed hash codes: ', len(bucket_sizes))
    print('Sizes of top 10 fullest buckets:')
    print(bucket_sizes[: 10])
    print('Trying to find house and ahahahahaha, deleting them, trying to find them again:')
    print(hash_table.find_word('house'))
    print(hash_table.find_word('ahahahahaha'))
    hash_table.delete_word('house')
    hash_table.delete_word('ahahahahaha')
    print(hash_table.find_word('house'))
    print(hash_table.find_word('ahahahahaha'))   
