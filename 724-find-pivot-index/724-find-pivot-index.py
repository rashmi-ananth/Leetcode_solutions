class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        left = 0
        right = sum(nums) - nums[0]
        
        for i in range(len(nums)):
            if left == right:
                return i
            else:
                left += nums[i]
                if i + 1<= len(nums) - 1:
                    right -= nums[i+1]
                else:
                    return -1
        return left == right
                
        
