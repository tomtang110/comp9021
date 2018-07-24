# Written by Eric Martin for COMP9021


'''
Deque abstract data type
'''


class EmptyDequeError(Exception):
    def __init__(self, message):
        self.message = message

    
class Deque:
    min_capacity = 10
    
    def __init__(self, capacity = min_capacity):
        self.min_capacity = capacity
        self._data = [None] * capacity
        self._length = 0
        self._front = 1
        
    def __len__(self):
        '''
        >>> len(Deque(100))
        0
        '''
        return self._length

    def is_empty(self):
        return self._length == 0

    def peek_at_front(self):
        '''
        >>> deque = Deque()
        >>> deque.peek_at_front()
        Traceback (most recent call last):
        ...
        EmptyDequeError: Cannot peek at front of empty deque
        '''
        if self.is_empty():
            raise EmptyDequeError('Cannot peek at front of empty deque')
        return self._data[self._front]

    def peek_at_back(self):
        '''
        >>> deque = Deque()
        >>> deque.peek_at_back()
        Traceback (most recent call last):
        ...
        EmptyDequeError: Cannot peek at back of empty deque
        '''
        if self.is_empty():
            raise EmptyDequeError('Cannot peek at back of empty deque')
        return self._data[(self._front + self._length - 1) % len(self._data)]

    def add_at_front(self, datum):
        '''
        >>> deque = Deque(1)
        >>> deque.add_at_front(0)
        >>> deque.peek_at_front()
        0
        >>> print(len(deque._data))
        1
        >>> deque.add_at_front(1)
        >>> deque.peek_at_front()
        1
        >>> print(len(deque._data))
        2
        >>> deque.add_at_front(2)
        >>> deque.peek_at_front()
        2
        >>> print(len(deque._data))
        4
        >>> deque.add_at_front(3)
        >>> deque.peek_at_front()
        3
        >>> print(len(deque._data))
        4
        >>> deque.add_at_front(4)
        >>> deque.peek_at_front()
        4
        >>> print(len(deque._data))
        8
        '''
        if self._length == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = datum
        self._length += 1

    def add_at_back(self, datum):
        '''
        >>> deque = Deque(1)
       >>> deque.add_at_back(0)
        >>> deque.peek_at_back()
        0
        >>> print(len(deque._data))
        1
        >>> deque.add_at_back(1)
        >>> deque.peek_at_back()
        1
        >>> print(len(deque._data))
        2
        >>> deque.add_at_back(2)
        >>> deque.peek_at_back()
        2
        >>> print(len(deque._data))
        4
        >>> deque.add_at_back(3)
        >>> deque.peek_at_back()
        3
        >>> print(len(deque._data))
        4
        >>> deque.add_at_back(4)
        >>> deque.peek_at_back()
        4
        >>> print(len(deque._data))
        8
        '''
        if self._length == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._front + self._length) % len(self._data)] = datum
        self._length += 1

    def remove_from_front(self):
        '''
        >>> deque = Deque(4)
        >>> for i in range(9): deque.add_at_front(i)
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_front())
        8
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_front())
        7
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_front())
        6
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_front())
        5
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_front())
        4
        >>> print(len(deque._data))
        8
        >>> print(deque.remove_from_front())
        3
        >>> print(len(deque._data))
        8
        >>> print(deque.remove_from_front())
        2
        >>> print(len(deque._data))
        4
        >>> print(deque.remove_from_front())
        1
        >>> print(len(deque._data))
        4
        >>> print(deque.remove_from_front())
        0
        >>> print(len(deque._data))
        4
        >>> print(deque.remove_from_front())
        Traceback (most recent call last):
        ...
        EmptyDequeError: Cannot remove from front of empty deque
        '''
        if self.is_empty():
            raise EmptyDequeError('Cannot remove from front of empty deque')
        datum_at_front = self._data[self._front]
        # Not necessary, only done to possibly hasten garbage collection
        # of element being removed from the deque.
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)        
        self._length -= 1
        self._shrink_if_needed()
        return datum_at_front

    def remove_from_back(self):
        '''
        >>> deque = Deque(4)
        >>> for i in range(9): deque.add_at_back(i)
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_back())
        8
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_back())
        7
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_back())
        6
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_back())
        5
        >>> print(len(deque._data))
        16
        >>> print(deque.remove_from_back())
        4
        >>> print(len(deque._data))
        8
        >>> print(deque.remove_from_back())
        3
        >>> print(len(deque._data))
        8
        >>> print(deque.remove_from_back())
        2
        >>> print(len(deque._data))
        4
        >>> print(deque.remove_from_back())
        1
        >>> print(len(deque._data))
        4
        >>> print(deque.remove_from_back())
        0
        >>> print(len(deque._data))
        4
        >>> print(deque.remove_from_back())
        Traceback (most recent call last):
        ...
        EmptyDequeError: Cannot remove from back of empty deque
        '''
        if self.is_empty():
            raise EmptyDequeError('Cannot remove from back of empty deque')
        index_at_back = (self._front + self._length - 1) % len(self._data)
        datum_at_back = self._data[index_at_back]
        # Not necessary, only done to possibly hasten garbage collection
        # of element being removed from the deque.
        self._data[index_at_back] = None
        self._length -= 1
        self._shrink_if_needed()
        return datum_at_back

    def _resize(self, new_size):
        # In any case, the element at position self._front will be at position 0 in new list.
        end = self._front + new_size
        # We are shrinking to a smaller list, and not wrapping in original list.
        if end <= len(self._data):
            self._data = self._data[self._front: end]
        # We are shrinking to a smaller list, but wrapping in original list.
        elif new_size <= len(self._data):
            # There are len(self._data) - self._front data in self._data[self._front: ],
            # and new_size - (len(self._data) - self._front) == end - len(self._data).
            self._data = self._data[self._front: ] + self._data[: end - len(self._data)]
        # We are expanding to a larger list.
        else:
            # The first two lists have a total length of len(self._data).
            self._data = (self._data[self._front: ] + self._data[: self._front] +
                          [None] * (new_size - len(self._data)))
        self._front = 0

    def _shrink_if_needed(self):
        # When the deque is one quarter full, we reduce its size to make it half full,
        # provided that it would not reduce its capacity to less than the minimum required.
        if self.min_capacity // 2 <= self._length <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()    
