class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(0,1),(1,0), (0,-1), (-1,0)]
        
        def dfs(i, j, visited):
       
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
                return
            
            if (i,j) in visited or image[i][j] != val:
                return
            
            image[i][j] = color
            visited.add((i,j))
            
            for x, y in directions:
                dfs(i+x, j+y, visited)
                
            
            
            
            
          
        val = image[sr][sc]
        dfs(sr, sc, set())
        return image
        