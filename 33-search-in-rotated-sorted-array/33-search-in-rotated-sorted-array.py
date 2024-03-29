class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # 8,9,1,2,3,4,5
        
        while l <= r:
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return -1
                
        
        
        