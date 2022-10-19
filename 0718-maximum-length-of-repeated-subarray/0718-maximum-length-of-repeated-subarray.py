class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        
        
        for i in range(len(nums1) -1, -1, -1):
            for j in range(len(nums2) -1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
 
               
            
        max_val = 0

        for i in range(len(dp)):
            curr_max = max(dp[i])
            max_val = max(max_val, curr_max)
            
        return max_val
            
        
        
