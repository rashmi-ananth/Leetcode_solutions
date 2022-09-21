class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
     # [4,5,6,7,8,0,1,2]
# [7,0,1,2,4,5,6]
    
    
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1           
                
            
    
    
    
    
    
    
    