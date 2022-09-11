class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        
        counter = 0
        nums.sort()
        nums.reverse()
        
        for i in range(len(nums)):
            val = nums[i]
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                if nums[l] + nums[r] <= val:
                    r -= 1
                    
                else:
                    counter += r - l
                    l += 1
                
            
        return counter    

        
        
# 4 3 3 2 2

# 4
# l r
# 3 1 = 4 <= 4
# 3 2 = 5 > 4 -
# 3 2 = 5 > 4 -

# l r
# 3 2 = 5 > 4 -
# # if less than or equal to r -= 1
# # if greater than l += 1 and add r - j





        
        
        