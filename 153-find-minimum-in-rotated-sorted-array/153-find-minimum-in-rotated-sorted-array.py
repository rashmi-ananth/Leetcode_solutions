class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def binary_search(nums, l, r):
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[r] >= nums[mid]:
                return binary_search(nums, l, mid - 1)
            else:
                return binary_search(nums, mid + 1, r)

        return binary_search(nums, 0, len(nums) - 1)	
    

    