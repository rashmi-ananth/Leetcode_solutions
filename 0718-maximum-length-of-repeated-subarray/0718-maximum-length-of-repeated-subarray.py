class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        
        
        for i in range(len(nums1) -1, -1, -1):
            for j in range(len(nums2) -1, -1, -1):
                
                if nums1[i] == nums2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                    
        max_repeat = 0
        for i in range(len(memo)):
            curr_max = max(memo[i])
            max_repeat = max(max_repeat, curr_max)
            
        return max_repeat