class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        
        chars = []
        count = []
        idx = 0
        
        while idx < len(s):
            if len(chars) != 0 and s[idx] == chars[-1]:
                chars.append(s[idx])
                count[-1] += 1
            else:
                chars.append(s[idx])
                count.append(1)
                
            
            if count[-1] == k:
                count.pop()
                for i in range(k):
                    chars.pop()
            idx += 1
           
        return ''.join(chars)
        
                
            
                
            

                
                
            
        
        
        