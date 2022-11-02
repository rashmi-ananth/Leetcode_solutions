# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        lst = []
        for i in range(len(lists)):
            curr = lists[i]
            while curr != None:
                lst.append(curr.val)
                curr = curr.next
                
        lst.sort()
        dummy = ListNode()
        curr = dummy
        for i in range(len(lst)):
            curr.next = ListNode(lst[i])
            curr = curr.next
        
        return dummy.next
        