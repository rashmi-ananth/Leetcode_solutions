class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1:
            return -1
        
        def dfs(i, visted, adj_lst):
            
            if i in visited:
                return
            visited.add(i)
            for j in adj_lst[i]:
                dfs(j, visited, adj_lst)
            
  
        adj_lst = dict()
        for i in range(n):
            adj_lst[i] = []
            
        for i, j in connections:
            adj_lst[i].append(j)
            adj_lst[j].append(i)
            
        visited = set()
        count = 0
        for i in adj_lst.keys():
            if i not in visited:
                dfs(i, visited, adj_lst)
                count += 1
                
        diff = len(connections) - count
        print(count, len(connections))


        return count - 1
        
                
        