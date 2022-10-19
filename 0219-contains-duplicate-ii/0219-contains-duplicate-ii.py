class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        nearby = set()
        
        for i in range(len(nums)):
            if nums[i] in nearby:
                return True
            
            nearby.add(nums[i])
            if len(nearby) > k:
                nearby.remove(nums[i-k])
                
        return False
        
        
        
        