class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
        
class linkedlist:
    def __init__(self,L=None,key = lambda x: x):
        self.key = key
        if not L:
            self.head = None
            self.length = 0
        else:
            self.head = Node(L[0])
            node = self.head
            self.length = 1
            for e in L[1:]:
                new_node = Node(e)
                node.next=new_node
                node = new_node
                self.length += 1
    def __len__(self):
##        if not self.head:
##            return 0
##        length = 1
##        node = self.head.next
##        while node:
##            length += 1
##            node = node.next
        return self.length
##
    def print_list(self,separator=','):
        if self.head:
            nodes = [str(self.head.value)]
            node =self.head.next
            while node:
                nodes.append(str(node.value))
                node = node.next
            print(separator.join(nodes))
    def extend(self,LL):
        if not self.head:
            self.head = LL.head
            return 
        node = self.head
        while node.next:
            node=node.next
        node.next = LL.head
    def is_sorted(self):
        if len(self) < 2:
            return True
        node = self.head
        # for as long as the current nde has a following node:
        while node.next:
            if self.key(node.next.value) < self.key(node.value):
                return False
            node = node.next
        return True
    def delete_e(self,to_delete):
        if not self.head:
            return
        if self.head.value == to_delete:
            self.head = self.head.next
            return
        node =self.head
        while node.next and node.next.value != to_delete:
            node = node.next
        if node.next:
            node.next = node.next.next
    def reverse(self):
        if len(self)<2:
            return
        R=self.head
        node = self.head.next
        self.head.next = None
        while node.next:
            next_node = node.next
            node.next = R
            R=node
            node = next_node
        node.next = R
        self.head = node
    def recursive_reverse(self):
        if len(self) < 2:
            return
        node =self.head
        while node.next.next:
            node = node.next
        new_head = node.next
        node.next = None
        self.recursive_reverse()
        new_head.next = self.head
        
        
b=linkedlist(L=[1,2,3,4,5])
b.reverse()     
b.print_list()     
            
        
            
            
                
        
