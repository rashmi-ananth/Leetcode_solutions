class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def dfs(i, adj_lst, visited, lst):
            
            if i in visited:
                return lst
            visited.add(i)
            lst.append(i)
            
            for j in adj_lst[i]:
                dfs(j, adj_lst, visited, lst)
                
            return lst
            
        
#         def bfs(i, adj_lst):
            
#             queue = [i]
#             lst = []
#             visited = set()
            
#             while len(queue) != 0:
#                 val = queue.pop(0)
                
#                 if val not in visited:
#                     lst.append(val)
#                 visited.add(val)
#                 for j in adj_lst[val]:
#                     queue.append(j)

#             return sorted(lst[1:])
        
        adj_lst = dict()
        for i in range(n):
            adj_lst[i] = []
            
        for a, b in edges:
            adj_lst[b].append(a)
            
         
        ancestors = []
        for i in range(n):
            lst = dfs(i, adj_lst, set(), [])
            ancestors.append(sorted(lst[1:]))
            # ancestors.append(bfs(i, adj_lst))
        
        return ancestors
            

                
                
                
                
                
                
                
                
                
                
            