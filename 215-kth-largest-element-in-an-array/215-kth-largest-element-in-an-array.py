from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        h = []
        for i in range(len(nums)):
            heappush(h, -nums[i])

        i = 0
        while i < k:
            val = heappop(h)
            i += 1
        return -val
        
        
        