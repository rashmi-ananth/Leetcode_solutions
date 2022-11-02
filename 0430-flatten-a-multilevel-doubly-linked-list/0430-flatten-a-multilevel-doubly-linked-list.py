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
        
        dummy = Node(-1, None, None, None)
        if head == None:
            return head
        
        stack = [head]
        curr = dummy
        while len(stack) != 0:
            node = stack.pop()
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
            curr.next = node
            node.prev = curr
            curr = curr.next
            curr.child = None
            
            
        dummy.next.prev = None
        return dummy.next
            
            
            
                
