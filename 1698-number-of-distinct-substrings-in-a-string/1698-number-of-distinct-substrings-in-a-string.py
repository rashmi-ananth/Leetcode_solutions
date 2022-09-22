class Solution:
    def countDistinct(self, s: str) -> int:
        
        
        distinct = set()
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                distinct.add(s[i:j])
        
        
        return len(distinct)