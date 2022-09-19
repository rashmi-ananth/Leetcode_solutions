class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        

        
        curr_idx = 0
        next_idx = 0
        
        
        while curr_idx < len(nums):
            
            if nums[curr_idx] != val:
                nums[next_idx] = nums[curr_idx]
                next_idx += 1
            curr_idx += 1
            
    
        return next_idx
        