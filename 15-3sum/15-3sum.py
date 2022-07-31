class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        lst = []
        nums.sort()
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            val = nums[i]
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                if nums[l] + nums[r] + val == 0:
                    lst.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                   
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                elif nums[l] + nums[r] + val < 0:
                    l += 1
                else:
                    r -= 1
                    
                    

        return lst
        
        
        
       # -4 -1 -1 0 1 2 
        
        