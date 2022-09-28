class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
#         0 2 5 4 4 
        
#         0 2 4 1 6
        
#         4 2 3

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if  i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                    break
                else:
                    print(i)
                    nums[i] = nums[i+1]
                    break
         
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return False
            
        return True
            
        