class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(i, j, count, visited):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return count
            
            if (i,j) in visited:
                return count
            
            visited.add((i,j))
            if grid[i][j] == 0:
                return count
            
            grid[i][j] = 0
            count += 1
            
            max_count = count
            for x,y in directions:
                max_count = max(max_count, dfs(i+x, j+y, max_count, visited))

                
            return max_count
            

        
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = dfs(i, j, 0, set())

                    max_count = max(max_count, count)
                   
  
        
        
        return max_count
        
        
        
        