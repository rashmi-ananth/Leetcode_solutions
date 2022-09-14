# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode(-1, None)
        carry = 0
        curr = dummy_node
        
        while l1 != None and l2 != None:
            
            total = l1.val + l2.val + carry
            curr.next = ListNode(total % 10, None)
            carry = total // 10
            curr = curr.next
            
            l1 = l1.next
            l2 = l2.next
            
        if l1 != None:
            while l1 != None:
                total = l1.val + carry
                curr.next = ListNode(total % 10, None)
                carry = total // 10
                curr = curr.next

                l1 = l1.next

            
        if l2 != None:
            while l2 != None:
                total = l2.val + carry
                curr.next = ListNode(total % 10, None)
                carry = total // 10
                curr = curr.next

                l2 = l2.next
        if carry:
            curr.next = ListNode(carry, None)
            
        return dummy_node.next  
        
        
      
                
                
                
                
                
            
        
