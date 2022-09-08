class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        pairings = dict()
        
        for i in range(len(pairs)):
            pairings[pairs[i][0]] = pairs[i][1]
            pairings[pairs[i][1]] = pairs[i][0]
            
        counter = 0
        unhappy = set()
        for i in range(n):
            paired = pairings[i]
            idx_paired = preferences[i].index(paired)
            
            for j in range(len(preferences[i])):
                if j == idx_paired:
                    continue
                val = preferences[i][j] 
                curr_idx = preferences[val].index(i)
                paired_v_idx = preferences[val].index(pairings[val])
                
                if j < idx_paired and curr_idx < paired_v_idx:
                  
                    unhappy.add(i)
        
        return len(unhappy)
                    
        
        
        
        
        
        
        
        
        
#         0:1
#         1:0
#         2:3
#         3:2
        
#         idx 0 = 2
        
        
        
#         x: 1
#         y: 0
#         u: 3
#         v: 2
        