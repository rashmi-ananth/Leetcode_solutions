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
        
        if not head:
            return None
        
        pseudoprev = Node(0,None,head,None)
        prev = pseudoprev
        stack = [head]
        
        while stack:
            curr = stack.pop()
            
            
            curr.prev = prev
            prev.next = curr
            
   
            if curr.next:
                stack.append(curr.next)
                
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            
            prev = curr
            
        pseudoprev.next.prev = None
        return pseudoprev.next
        
       
        
            
        