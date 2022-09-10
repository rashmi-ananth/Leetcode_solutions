class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        
        nums.sort()
        curr_total = sum(nums[:3])
        
        for i in range(len(nums)):
            l,r = i+1, len(nums) - 1
            curr = nums[i]
            while l < r:  
                total = nums[l] + nums[r] + curr
                if total == target:
                    return total
                if abs(total-target) < abs(curr_total-target):
                    curr_total = total 
                if total < target:
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                else:
                    r -= 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
            if curr_total == target:
                break
            
        return curr_total
                
                
            
            
            
            
            
        