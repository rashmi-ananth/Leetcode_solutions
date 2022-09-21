class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
        
        count = 0
        for char in s_dict.keys():
            if char not in t_dict.keys():
                count += s_dict[char]
            else:
                if s_dict[char] > t_dict[char]:
                    count += s_dict[char] - t_dict[char]
        return count
                    
                
        
        abb
        aab
        
        
        
#         aab
#         abb
        
#         a:2 b:1
#         a:1 b:2
        
        
#     l:1 e:3 t:1 c:1 o:1 d:1
                            
#     p:1 r:1 a:1 c:2 t:1 i:1 e:1
                                
                                
                                
#     1 + 2 + 0 + 0 + 1 + 1
    
#     total = 0
#     if s[key] not in t.keys:
#         total += s[key]
#     else:
#         if s[key] > t[key]:
#             total += s[key] - t[key]
        
        
        
        