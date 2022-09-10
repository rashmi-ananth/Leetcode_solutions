# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        
        # traverse through list to find length of list
        # traverse through list a second time to find len - nth
            # node of the list
        # switch pointers to remove nth node
        
        counter = 0
        while curr != None:
            curr = curr.next
            counter += 1
            
            
        ptr1 = head
        ptr2 = head.next
        
        desired_node = counter - n
        
        
        if desired_node == 0:
            ptr1.next = None
            return ptr2
        counter2 = 1
        
        while ptr2 and counter2 < desired_node:
            ptr1 = ptr2
            ptr2 = ptr2.next
            counter2 += 1
            
        ptr1.next = ptr2.next
        ptr2.next = None
        
        return head
        
        
        
            
            
            
            
            
            
            
            
            