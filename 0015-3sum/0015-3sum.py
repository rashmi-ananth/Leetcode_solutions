class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Time: O(n^2)
        # Space: O(N)
        
        return_lst = []
        nums.sort()
        i = 0

        
        while i < len(nums):
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    return_lst.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    r -= 1
                    while r > l and nums[r+1] == nums[r]:
                        r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
            
            i += 1
            while i < len(nums) and nums[i-1] == nums[i]:
                i += 1       
        
        return return_lst