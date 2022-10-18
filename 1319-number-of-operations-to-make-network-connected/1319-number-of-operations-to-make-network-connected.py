class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1:
            return -1
        def dfs(i, adj_lst, visited):
            
            if i in visited:
                return
            visited.add(i)
            for j in adj_lst[i]:
                dfs(j, adj_lst, visited)
            
            
#             queue = [i]
            
#             while len(queue) > 0:
#                 val = queue.pop(0)
#                 visited.add(val)
                
#                 for j in adj_lst[val]:
#                     if j not in visited:
#                         queue.append(j) 
#             return visited
        
        
        adj_lst = dict()
        for i in range(n):
            adj_lst[i] = []
            
        for i in range(len(connections)):
            adj_lst[connections[i][0]].append(connections[i][1])
            adj_lst[connections[i][1]].append(connections[i][0])
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, adj_lst, visited)
                count += 1
                
        
        if count == 1:
            return 0
        
        diff = len(connections) - count 

        return count-1
                
            
        