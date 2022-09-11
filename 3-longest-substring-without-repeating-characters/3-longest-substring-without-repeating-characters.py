class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        dictionary = defaultdict(int)
        curr_len = 0
        best_len = 0
        
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            char = s[i]
            if char in dictionary.keys() and dictionary[char] >= start:
                start = dictionary[char] + 1
                best_len = max(best_len, curr_len)
                curr_len = 0
                dictionary[char] = i
                
            else:
                dictionary[char] = i
                curr_len = i - start + 1
        best_len = max(best_len, curr_len)     
        return best_len
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        