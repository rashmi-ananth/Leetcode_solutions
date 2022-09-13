class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        def binary_search(l,r):
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if l == r:
                return -1
            if nums[mid] < target:
                return binary_search(mid + 1,r)

            return binary_search(l,mid)
 

        return binary_search(0,len(nums) - 1)