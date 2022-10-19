class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        
        prev_sums = {0:-1}
        curr_sum = 0
        max_len = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in prev_sums:
                length = i - prev_sums[curr_sum - k]
                max_len = max(max_len, length)
                
            if curr_sum not in prev_sums:
                prev_sums[curr_sum] = i
                
        return max_len
                
            
        
        

            
           
        
        