# Written by *** for COMP9021


from binary_tree_adt import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def _bubble_up(self,last_node=None):
        if last_node == None or last_node.value <= self.value:
            return True
        if last_node.value > self.value:
            last_node.value, self.value = self.value, last_node.value
            return True
    def insert(self, value,last_node=None):
        new_value = value
        size =self.size()
        if self.value == None:
            total_height =0 
            total_node = 0
        else:
            total_height =self.height()
            total_node = (1-2**total_height*2)//(1-2)        
        if self.value == None:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
            self._bubble_up(last_node)
            return True

        size_left = self.left_node.size()
        size_right = self.right_node.size()
        if self.left_node.value == None:
            height_left = 0
            node_left_nb = 0
        else:
            height_left = self.left_node.height()
            node_left_nb = (1-2**height_left*2)//(1-2)
        if self.right_node.value == None:
            height_right = 0 
            node_right_nb = 0 
        else:
            height_right = self.right_node.height()
            node_right_nb = (1-2**height_right*2)//(1-2)

        if total_node == size:
            if self.value > value:
                new_value,self.value = self.value, value
            self.left_node.insert(new_value,self)
            return True
        if node_left_nb == size_left:
            if self.value > value:
                new_value,self.value = self.value,value
            self.right_node.insert(new_value,self)
            return True
        if size_left < node_left_nb:
            if self.value > value:
                new_value, self.value = self.value , value
            self.left_node.insert(new_value,self)
            return True
        if size_right < node_right_nb:
            if self.value > value:
                new_value, self.value = self.value , value
            self.right_node.insert(new_value,self)
            return True
    
        # Replace pass above with your code