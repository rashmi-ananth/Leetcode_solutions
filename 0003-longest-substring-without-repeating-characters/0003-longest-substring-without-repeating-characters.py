class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        dictionary = dict()
        max_length = 0
        curr_len = 0
        
        for i in range(len(s)):
            if s[i] not in dictionary.keys() or dictionary[s[i]] < start:
                dictionary[s[i]] = i
                curr_len = i - start + 1
                max_length = max(max_length, curr_len)
                
            else:
                
                start = dictionary[s[i]] + 1
                
                curr_len = 0
                dictionary[s[i]] = i
                        
                
        max_length = max(max_length, curr_len)
        return max_length
