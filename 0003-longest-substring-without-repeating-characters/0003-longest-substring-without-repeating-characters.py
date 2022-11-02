class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dictionary = dict()
        start = 0
        curr_len = 0
        max_len = 0
        
        for i in range(len(s)):
            if s[i] not in dictionary or dictionary[s[i]] < start:
                dictionary[s[i]] = i
                curr_len = i - start + 1
                max_len = max(max_len, curr_len)
                
            else:
                start = dictionary[s[i]] + 1
                dictionary[s[i]] = i
                curr_len = i - start + 1
        
        
        max_len = max(max_len, curr_len)
        return max_len
        