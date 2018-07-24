# Written by **** for COMP9021


from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        if len(self) < 3:
            return
        R = self.head
        min_num=10000000
        while R:
            if R.value < min_num:
                min_num = R.value
            R = R.next_node           
        Q=self.head
        
        if Q.value == min_num:
            pass
        else:
            while Q.next_node:
                if Q.next_node.value != min_num:
                    Q = Q.next_node
                else:
                    K = Q.next_node
                    Q.next_node = None
        K1 = K
        while K.next_node:
            K=K.next_node
        K.next_node = self.head
        self.head = K1
        A=self.head
        length = 0 
        while A.next_node:
            length += 1
            A = A.next_node
        second_order = length -1
        A = self.head
        length = 0 
        while length != second_order:
            length += 1
            A = A.next_node
        B = A.next_node
        A.next_node = None
        B.next_node = self.head
        self.head = B
        C=self.head
        C1 = C.next_node
        C.next_node = None
        C2 = C1.next_node
        C1.next_node = None
        G1 = C1
        C1.next_node = C
        C3 = C2.next_node
        C2.next_node = None
        C4 = C3.next_node
        C3.next_node = None
        C1.next_node.next_node = C3
        C1.next_node.next_node.next_node = C2
        C1 = C1.next_node.next_node.next_node
        
        if C4 is not None:
            while C4.next_node:
                C5 = C4.next_node
                C4.next_node = None
                if not C5.next_node:
                    C1.next_node = C5
                    C1.next_node.next_node = C4
                    C4 = C1.next_node.next_node
                    break
                else:
                    C6 = C5.next_node
                    C5.next_node = None
                    C1.next_node = C5
                    C1.next_node.next_node = C4
                    C1 = C1.next_node.next_node
                    C4 = C6
        else:
            self.head = G1
        self.head = G1

