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
        
        
        prev_orig = Node(0, None, head, None)
        prev = prev_orig
        stack = [head]
        
        while len(stack) > 0:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            if curr.next != None:
                stack.append(curr.next)
            if curr.child != None:
                stack.append(curr.child)
                
                curr.child = None
            prev = curr
         
        prev_orig.next.prev = None
        return prev_orig.next
        
        
        
      
       
        
            
        