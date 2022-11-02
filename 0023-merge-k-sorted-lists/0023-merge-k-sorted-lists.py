from heapq import heapify, heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Time: O(nlogk)
        # Space: O(K)
        
        if len(lists) == 0:
            return None
        
        h = []
        heapify(h)
        counters = [None] * len(lists)
        
        dummy = ListNode()
        for i in range(len(lists)):
            counters[i] = lists[i]
            if lists[i] != None:
                heappush(h, (lists[i].val, i))

        
        curr = dummy
        while len(h) > 0:
            val, idx = heappop(h)
            curr.next = counters[idx]
            counters[idx] = counters[idx].next
            if counters[idx] != None:
                heappush(h, (counters[idx].val, idx))
            curr = curr.next

        return dummy.next
