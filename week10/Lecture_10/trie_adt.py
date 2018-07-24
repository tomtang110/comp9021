# Written by Eric Martin for COMP9021


'''
A particular case of general trees: tries
'''


from collections import defaultdict


class Trie:
    '''
    >>> trie = Trie()
    >>> for word in ['he', 'hers', 'has', 'heir', 'one']: trie.add_word(word)
    >>> trie.has_been_recorded('he')
    True
    >>> trie.has_been_recorded('her')
    False
    >>> trie.has_been_recorded('hers')
    True
    >>> trie.has_been_recorded('one')
    True
    >>> trie.has_been_recorded('two')
    False
    '''
    def __init__(self):
        self.is_word = False
        self.extensions = defaultdict(Trie)

    def add_word(self, word):
        current_trie = self
        for c in word:
            current_trie = current_trie.extensions[c]
        current_trie.is_word = True

    def has_been_recorded(self, word):
        current_trie = self
        for c in word:
            if c not in current_trie.extensions:
                return False
            current_trie = current_trie.extensions[c]
        return current_trie.is_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()        
                
