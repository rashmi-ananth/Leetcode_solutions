class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

    
        counter = 0
        val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == val:
                nums[i] = '_'
                counter += 1
            else:
                val = nums[i]
           
        i = 0
        placement = 0
        while i < len(nums):
            if nums[i] != '_':
                nums[placement] = nums[i]
                placement += 1
            i += 1
        
        return len(nums) - counter
        
        
                
        