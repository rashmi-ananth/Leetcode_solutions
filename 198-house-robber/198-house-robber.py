class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if len(nums) < 2:
            return nums[0]

        prev1 = 0
        prev2 = 0
        
        
        for i in range(len(nums)):
            temp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = temp
        

        return prev1





        

            
            
            
        
        