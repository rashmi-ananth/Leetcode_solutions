# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # extract first num
        # extract second num
        # add the two
        # create reversed linked list of sum
        
        curr1 = l1
        num1 = 0
        factor = 1
        while curr1 != None:
            value = curr1.val
            num1 = num1 + factor*value
            curr1 = curr1.next
            factor *= 10
            
        curr2 = l2
        num2 = 0
        factor = 1
        while curr2 != None:
            value = curr2.val
            num2 = num2 + factor*value
            curr2 = curr2.next
            factor *= 10
            
        sum_val = num1 + num2
        
        dummy = ListNode()
        curr = dummy
        while sum_val >= 0:
            value = sum_val % 10
            node = ListNode(value)
            curr.next = node
            curr = curr.next
            sum_val = sum_val // 10
            
            if sum_val == 0:
                break
          
        return dummy.next
            
        
        
        
        
        
        
        
        
        
        
        
        
                
        

        
        
        
        
 