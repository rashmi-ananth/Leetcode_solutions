class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        s = s.split(" ")
        s.reverse()
        for i in range(len(s)):
            s[i] = s[i].strip()
        

        return_str = []
        
        for i in range(len(s)):
            if len(s[i]) == 0:
                continue
            return_str.append(s[i])
            
        return ' '.join(return_str)
        