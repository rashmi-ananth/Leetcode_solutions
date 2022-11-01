class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
    
        arr = [nums[0]]
        
        for i in range(1, len(nums)):
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            
        return max(arr)
        
        
        
        
        