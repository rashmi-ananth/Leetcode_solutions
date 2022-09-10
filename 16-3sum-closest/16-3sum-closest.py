class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        
        diff = float('inf')
        ans = 0
        l = len(nums)
        
        nums.sort()
        for i in range(l):
            lo = i + 1
            hi = l - 1
            
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                d = abs(target - s)
                if d == 0:
                    return s
                if d < diff:
                    diff = d
                    ans = s
                if s < target:
                    lo += 1
                else:
                    hi -= 1
        return ans
                
                
            
            
            
            
            
        