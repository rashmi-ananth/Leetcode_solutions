import numpy as np
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]
        
        
#         if sum(nums) % 2 != 0:
#             return False
#         if len(nums) == 1:
#             return False
        
#         target_sum = sum(nums) // 2
#         dp = np.zeros((len(nums), target_sum + 1))
#         if nums[0] <= target_sum:
#             dp[0][nums[0]] = 1
#         dp[0][0] = True
 
#         for i in range(1, len(dp)):
#             for j in range(1, len(dp[0])):
                
#                 if j < nums[i]:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = max(dp[i-1][j - nums[i]], dp[i-1][j])
                    
         
 
#         return dp[-1][-1] == 1
                    
                
        #     0   1   2   3   4
        # 1   1   1   0   0   0
        # 2   1   1   1   1   0
        # 5   1   1   1   1   0
        
        
        #     0   1   2   3   4   5   6   7   8   9   10  11
        # 1   1   1   0   0   0   0   0   0   0   0   0   0
        # 5   1   1   0   0   0   1   1   0   0   0   0   0
        # 11  1   1   0   0   0   1   1   0   0   0   0   1
        # 5   1   1   0   0   0   1   1               1   1
        
        
        