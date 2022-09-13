# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return head
        
        curr = head
        counter = 0
        while curr != None:
            counter += 1
            curr = curr.next
        curr = head
    
        half = counter // 2 - 1
            
        while half > 0:
            curr = curr.next
            half -= 1
        
        new_curr = curr.next
        curr.next = None
        
        
        prev = None
        temp = new_curr.next
        
        while new_curr != None:
            temp = new_curr.next
            new_curr.next = prev
            prev = new_curr
            new_curr = temp
        curr = head
        
        while prev.next != None and curr.next != None:
            temp1 = prev.next
            temp2 = curr.next
            curr.next = prev
            prev.next = temp2
            curr = temp2
            prev = temp1
        
            
        if curr != None:
            curr.next = prev
            

            
        
        
        
        
        
#     1    2   3
#     5   4   3
        
            

        
        
        
        
        
        
# 1   2   3   4   5

# 1   5   2   4   3

# start = 2
# end = 4

# temp = start.next
# temp2 = end.next
# start.next = end
# end.next = temp
# start = temp
# end = temp2






