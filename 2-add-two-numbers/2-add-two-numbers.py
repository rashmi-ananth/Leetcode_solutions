# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        4831
        251
        635
        curr = ListNode(-1, None)
        carry = 0
        dummy_node = curr
        
        while l1 != None and l2 != None:
            
            total = l1.val + l2.val + carry
            dummy_node.next = ListNode(total % 10, None)
            carry = total // 10
            dummy_node = dummy_node.next
            
            l1 = l1.next
            l2 = l2.next
            
        if l1 != None:
            while l1 != None:
                total = l1.val + carry
                dummy_node.next = ListNode(total % 10, None)
                carry = total // 10
                dummy_node = dummy_node.next

                l1 = l1.next

            
        if l2 != None:
            while l2 != None:
                total = l2.val + carry
                dummy_node.next = ListNode(total % 10, None)
                carry = total // 10
                dummy_node = dummy_node.next

                l2 = l2.next
        if carry:
            dummy_node.next = ListNode(carry, None)
            
        return curr.next  
        
        
      
                
                
                
                
                
            
        
