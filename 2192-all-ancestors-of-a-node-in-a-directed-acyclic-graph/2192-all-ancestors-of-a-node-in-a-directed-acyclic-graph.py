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
        
        return_lst = []
        for i in range(n):
            if i not in visited:
                dfs(i, visited, adj_lst)
         
        for i in range(n):
            return_lst.append(sorted(visited[i]))
                
         
        return return_lst
                
                
                
        