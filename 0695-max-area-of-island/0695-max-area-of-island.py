class Solution:
    def maxAreaOfIsland(self, grid):
        
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r, c + 1) 

        # t: O(rc) s: O(1)
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area
    
