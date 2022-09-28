class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if  i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                    break
                else:
                    nums[i] = nums[i+1]
                    break
         
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return False
            
        return True
            
        