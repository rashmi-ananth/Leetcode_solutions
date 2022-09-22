import numpy as np
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        if len(nums) == 1:
            return False
        
        target_sum = sum(nums) // 2
        #dp = np.zeros((len(nums), target_sum + 1))
        dp = []
        for i in range(len(nums)):
            dp.append([0] * (target_sum + 1))
        if nums[0] <= target_sum:
            dp[0][nums[0]] = 1
        dp[0][0] = 1
 
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j - nums[i]], dp[i-1][j])
                    
         
 
        return dp[-1][-1] == 1
                    
                
        #     0   1   2   3   4
        # 1   1   1   0   0   0
        # 2   1   1   1   1   0
        # 5   1   1   1   1   0
        
        
        #     0   1   2   3   4   5   6   7   8   9   10  11
        # 1   1   1   0   0   0   0   0   0   0   0   0   0
        # 5   1   1   0   0   0   1   1   0   0   0   0   0
        # 11  1   1   0   0   0   1   1   0   0   0   0   1
        # 5   1   1   0   0   0   1   1               1   1
        
        
        