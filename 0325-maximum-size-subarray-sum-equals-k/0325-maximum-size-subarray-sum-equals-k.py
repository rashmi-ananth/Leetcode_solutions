class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
       
        
        max_len = 0
        dictionary = {0:-1}
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            
            if total - k in dictionary.keys():
                max_len = max(max_len, i-dictionary[total - k])
                
            if total not in dictionary.keys():
                dictionary[total] = i
                
        return max_len
            
            
            
          