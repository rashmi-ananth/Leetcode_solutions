class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(i, j, count):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            return 1 + dfs(i, j+1, max_count) + dfs(i, j-1, max_count) + dfs(i+1, j, max_count) + dfs(i-1, j, max_count)


        
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = dfs(i, j, 0)

                    max_count = max(max_count, count)
                   
  
        
        
        return max_count
        
        
        
        