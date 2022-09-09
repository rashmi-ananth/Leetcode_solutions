class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        source = 0
        target = len(graph) - 1
        
        return_lst = []
        def dfs(source, path):
            
            if source == target:
                return_lst.append(path)
                return
            
            for i in range(len(graph[source])):
                dfs(graph[source][i], path + [graph[source][i]])
            
            
        dfs(source, [source])
        
        return return_lst
        
                
            
        
        