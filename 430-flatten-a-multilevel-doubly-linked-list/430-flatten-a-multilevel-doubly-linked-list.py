"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return head
        
        dummy = Node(0,None, None, None)
        stack = [head]
        curr = dummy

        while len(stack) > 0:
            
            node = stack.pop()
            
            if node.next != None:
                stack.append(node.next)
            if node.child != None:
                stack.append(node.child)  
                node.child = None
            
            curr.next = node
            node.prev = curr
            curr = node
        
        
        dummy.next.prev = None
        return dummy.next
            

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        