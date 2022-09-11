class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        
        nonzero = 0
        
        
        for i in range(len(nums)):
            
            if nums[i] != 0:
                nums[nonzero] = nums[i]
                nonzero += 1
        
        for i in range(nonzero, len(nums)):
            nums[i] = 0
            
        
        
        
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        

