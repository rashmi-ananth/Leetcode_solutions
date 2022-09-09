import numpy as np
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        
        s_counter = Counter(s)
        t_counter = Counter(t)
    
        
        answer = 0
        for i in s_counter.keys():
            
            if i not in t_counter.keys():
                answer += s_counter[i]
            elif s_counter[i] - t_counter[i] > 0:
                answer += s_counter[i] - t_counter[i]
                
        return answer
                
        
        
     
