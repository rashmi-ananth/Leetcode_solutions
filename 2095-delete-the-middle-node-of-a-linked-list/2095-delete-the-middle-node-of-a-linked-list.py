# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # find length of list
        # go to middle node
        # delete middle node
        
        counter = 0
        curr = head 
        
        while curr != None:
            counter += 1
            curr = curr.next
            
        prev = ListNode(0, head)
        curr_prev = prev
        curr = prev.next
        middle = counter // 2
        counter = 0
        
        while counter < middle:
            counter += 1
            
            curr_prev = curr_prev.next
            curr = curr.next
           
        temp = curr.next
        curr.next = None
        curr_prev.next = temp
        
        return prev.next
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        