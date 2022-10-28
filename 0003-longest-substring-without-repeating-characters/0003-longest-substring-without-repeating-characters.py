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
                max_length = max(max_length, curr_len)
                curr_len = 0
                dictionary[s[i]] = i
                
                
                
        max_length = max(max_length, curr_len)
        return max_length
    
    
    # "aegrhtsry etrwaesnr"
    # start = 4
    # 5
    # 7
    # {a:0, e:9, g:2, r:7, h:4, t:5 s:6, " ":8}
        