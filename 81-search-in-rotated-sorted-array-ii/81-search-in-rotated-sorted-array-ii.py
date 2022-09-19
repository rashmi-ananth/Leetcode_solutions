class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l += 1
                else:
                    r -= 1
                    
                
            else:
                if target > nums[r] or target < nums[mid]:
                    r -= 1
                else:
                    l += 1
        return False
                
        