class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        lst = [nums[0]]
        
        
        for i in range(1,len(nums)):
            lst.append(nums[i] + lst[-1])
            
        return lst