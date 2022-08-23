class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        
        
        length = len(nums)
        def findPeak(l, r, nums):
            
            mid = (l + r) // 2
            val = nums[mid]
            
            
            if ((mid + 1 < length and nums[mid + 1] < val) or mid + 1 >= length) and ((mid - 1 >= 0 and nums[mid - 1] < val) or mid - 1 < 0):
                return mid
            
            if mid + 1 < length and mid - 1 >= 0:
                if nums[mid + 1] > nums[mid - 1]:
                    return findPeak(mid + 1, r, nums)
                else:
                    return findPeak(l, mid, nums)
            elif mid + 1 < length:
                return findPeak(mid + 1, r, nums)
            else:
                return findPeak(l, mid, nums)
        
        return findPeak(0, length, nums)
                
                    
                
                
                
                
                
                
                
                
                
                
            
        