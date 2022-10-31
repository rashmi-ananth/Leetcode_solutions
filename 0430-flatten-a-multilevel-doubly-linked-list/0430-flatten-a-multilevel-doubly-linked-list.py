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
            return head
        
        stack = [head]
        dummy = Node(0, None, None, None)
        curr = dummy
        
        
        while len(stack) > 0:
            node = stack.pop()
            
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                
            curr.next = node
            node.prev = curr
            curr.child = None
            curr = curr.next
            
        
        dummy.next.prev = None
        return dummy.next
        