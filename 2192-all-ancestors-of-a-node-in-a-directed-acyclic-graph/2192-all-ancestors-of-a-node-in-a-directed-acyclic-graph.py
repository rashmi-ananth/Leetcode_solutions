class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        def dfs(i, visited, adj_lst):
            
            if i in visited.keys():
                return visited[i]
            
     
            for j in adj_lst[i]:
                visited[i] += [j] + dfs(j, visited, adj_lst)
            visited[i] = list(set(visited[i]))
                
            return visited[i]

        
        adj_lst = dict()
        for i in range(n):
            adj_lst[i] = []
            
        for i, j in edges:
            adj_lst[j].append(i)
            
        visited = defaultdict(list)
        for i in range(n):
            lst = dfs(i, visited, adj_lst)

        return_lst = []
        sorted_keys = sorted(visited)
        
        for key in sorted_keys:
            visited[key].sort()
            return_lst.append(visited[key])
            
        return return_lst
            
        
        
        
        
        
        
        