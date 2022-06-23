class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False
        
        counts = dict()
        for i in range(len(s)):
            if s[i] in counts.keys():
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
                

                
        for i in range(len(t)):
            if t[i] in counts.keys():
                counts[t[i]] -= 1
            else:
                return False
                
        for i in counts.keys():
            if counts[i] != 0:
                return False
        return True
        