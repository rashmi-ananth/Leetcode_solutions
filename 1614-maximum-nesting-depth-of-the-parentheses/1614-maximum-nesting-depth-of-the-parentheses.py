class Solution:
    def maxDepth(self, s: str) -> int:
        
        counter = 0
        max_count = 0
        
        
        for i in range(len(s)):
            if s[i] == '(':
                counter += 1
                max_count = max(max_count, counter)
            if s[i] == ')':
                counter -= 1
                
        return max_count
        