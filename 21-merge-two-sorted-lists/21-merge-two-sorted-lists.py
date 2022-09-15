# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2
        dummy = ListNode(0, None)
        curr = dummy
        
        while curr1 != None and curr2 != None:
            
            if curr1.val < curr2.val:
                temp = curr1.next
                curr.next = curr1
                curr1 = temp
            else:
                temp = curr2.next
                curr.next = curr2
                curr2 = temp
            curr = curr.next
            
        if curr1 != None:
            curr.next = curr1
            
        if curr2 != None:
            curr.next = curr2
            
        return dummy.next
    
    
  
            
        
        
        
        