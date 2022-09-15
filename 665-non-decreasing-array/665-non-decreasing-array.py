class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        count_large = 0

        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
     
                if i + 2 < len(nums):
                    if nums[i+2] < nums[i]:
            
                        nums[i] = nums[i+1]
               
                    else:
                        nums[i+1] = nums[i]
                else:
                     nums[i+1] = nums[i]
                    
            
                break
                
         
 
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
            
            
        return True
            

           
  
        

        