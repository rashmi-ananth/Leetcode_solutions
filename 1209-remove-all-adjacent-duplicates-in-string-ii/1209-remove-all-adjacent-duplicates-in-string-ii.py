class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        chars = [s[0]]
        counts = [1]
        
        for i in range(1, len(s)):
           
            if len(chars) > 0 and s[i] == chars[-1]:
                chars.append(s[i])
                counts[-1] += 1
                
                if counts[-1] == k:
                    counts.pop()
                    for j in range(k):
                        chars.pop()
      
            else:
                chars.append(s[i])
                counts.append(1)
        
        return ''.join(chars)
                
                
            
            
            
        


     
        
        
     
        
        
        