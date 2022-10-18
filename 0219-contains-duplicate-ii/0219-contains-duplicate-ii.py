class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        values = set()
        
        for i in range(len(nums)):
            
            if nums[i] in values:
                return True
            values.add(nums[i])
            
            if len(values) > k:
                values.remove(nums[i-k])
                
                
        return False