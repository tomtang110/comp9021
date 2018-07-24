class prioritylist:
    def __init__(self,capacity=20):
        self.capacity = capacity
        self.pq = [None]*(capacity+1)
        self.size = 0
    def insert(self,value):
        self.size += 1
        #IF self.size < self.capcacity
        #else self.pq needs to be extended
        self.pq[self.size] = value
        self._bubble_up(self.size)
    def _bubble_up(self,position):
        if position == 1:
            return
        parent_position = position // 2
        if self.pq[parent_position] < self.pq[position]:
            self.pq[parent_position],self.pq[position] = self.pq[position],self.pq[parent_position]
            self._bubble_up(parent_position)
    def process_top_element(self):
        element_being_processed = self.pq[1]
        self.pq[1], self.pq[self.size] = self.pq[self.size] , self.pq[1]
        self.size -= 1
        self._bubble_down(1)
    def _bubble_down(self,position):
        position_of_largest_child = 2* position
        if 2*position + 1 <= self.size and self.pq[2*position + 1]>self.pq[2*position]:
            position_of_largest_child += 1
        if 2*position <= self.size and self.pq[position_of_largest_child] > self.pq[position]:
            self.pq[position_of_largest_child],self.pq[position] = \
                                                self.pq[position],self.pq[position_of_largest_child]
            self._bubble_down(position_of_largest_child)
            
        
        
