class Tree:
    def __init__(self,value=None):
        self.value=value
        if value is None:
            self.left_subtree = None
            self.right_subtree = None
        else:
            self.left_subtree = Tree()
            self.right_subtree = Tree()
    def insert_in_bst(self,value):
        if self.value is None :
            self.value = value
            self.left_subtree = Tree()
            self.right_subtree = Tree()
            return True
        if value ==self.value:
            return False
        if value < self.value:
            return self.left_subtree.insert_in_bst(value)
        return self.right_subtree.insert_in_bst(value)
            
    def height(self):
        if self.value is None:
            return 0
        
        return max(self.left_subtree._height(),self.right_subtree._height())
    def _height(self):
        if self.value is None:
            return 0
        return max(self.left_subtree._height(),self.right_subtree._height())+1
    def display(self):
        self._display(0,self.height())
    def _display(self,level,height):
        if level > height:
            return
        if level==height:
            print('    '*height,self.value,sep='')
            return
        if self.left_subtree.value is not None:
            self.left_subtree._display(level+1,height)
        else:
            print('\n'*(2**(height-level)-1))
        print('    '*height,self.value,sep='')
        if self.right_subtree.value is not None:
            self.right_subtree._display(level+1,height)
        else:
            print('\n'*(2**(height-level)-1))
            
    def is_bst(self):
        if self.value is None:
            return True
        if self.left_subtree.value is not None:
            largest_smaller_tree = self.left_subtree
            while largest_smaller_tree.right_subtree.value is not None:
                largest_smaller_tree = largest_smaller_tree.right_subtree
                if largest_smaller_tree.tree>=self.value:
                    return False
                 
        if self.right_subtree.value is not None :
            largest_smaller_tree = self.left_subtree
            while largest_smaller_tree.right_subtree.value is not None:
                largest_smaller_tree = largest_smaller_tree.right_subtree
                if largest_smaller_tree.tree >= self.value:
                    return False
        return self.left_subtree.is_bst() and self.right_subtree.is_bst()
    
