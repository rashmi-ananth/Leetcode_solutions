class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
            
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for i in range(len(s)):
            s_dict[s[i]] += 1
        for i in range(len(t)):
            t_dict[t[i]] += 1
           
        counter = 0
        for key in s_dict.keys():
            if key not in t_dict:
                counter += s_dict[key]
            else:
                if s_dict[key] > t_dict[key]:
                    counter += s_dict[key] - t_dict[key]
        
        return counter
                
                
                
                
               
                
             
                