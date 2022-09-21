class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        # O(s)
        
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
                    
            
        
        