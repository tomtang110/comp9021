from stack_adt import *
def checks_parentheses_are_balanced(expression):
    stack = Stack()
    for s in expression:
        kinds_of_parentheses = {')':'(','}':'{',']':'['}
        if s in '([{':
            stack.push(s)
        elif s in ')]}':
            # stack is not empty: imbalanced
            # if ) top of stack should contain (
            # if ] top of stack should contain [
            # if } top of stack should contain {
##            if stack.is_empty():
##                return False
##            if kinds_of_parentheses[s] != stack.peek():
##                return False
##
            try:
                if kinds_of_parentheses[s] != stack.peek():
                    return False
            except EmptyStackError:
                return False
            #pop corresponding opening bracket from stack
            stack.pop()
    return stack.is_empty()
                    
def evaluate(expression):
    operations ={'+':lambda x,y:x+y,
                 '-':lambda x,y:y-x,
                 '*':lambda x,y:x*y,
                 '/':lambda x,y:y/x}
    stack=Stack()
    processing_number = False
    for s in expression:
        if s.isdigit():
            if not processing_number:
                processing_number = True
            #Push the first digit in a number that is possibly
            #many digits long
                stack.push(int(s))
            else:
            # s is another digit as part of a number whose previous
            # digits have been processed, and assembled into a number
            # which is now on top of our stack
                stack.push(stack.pop()*10+int(s))
        else:
            # either we just stop processing a number
            # or we stopped before; in any case, processing number
            # becomes False or is False already
            processing_number = False
            if s in operations:
                stack.push(operations[s](stack.pop(),stack.pop()))
    result= stack.pop()
    if not stack.is_empty():
        print('Expression incorrect')
    else:
        return result
                
            
            
            
