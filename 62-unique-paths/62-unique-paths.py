class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
    
        def dfs(i, j):
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if (i, j) in visited:
                return visited[(i, j)]
            if i == m-1 and j == n-1:
                return 1
            
            visited[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return visited[(i, j)]
            
            
            
        
        visited = dict()
        return dfs(0,0)
        