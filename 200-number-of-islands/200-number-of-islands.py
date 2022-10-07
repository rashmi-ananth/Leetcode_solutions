class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(i, j):
            
            if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[0]):
                return
            
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            
            for x,y in directions:
                dfs(i + x, j + y)
            
            return
            
            
            
        count = 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
                    
        return count
        