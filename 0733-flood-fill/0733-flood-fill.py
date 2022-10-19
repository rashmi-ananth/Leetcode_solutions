class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
                return
            
            if image[i][j] != orig_color:
                return
            if (i, j) in visited:
                return
            visited.add((i,j))
            image[i][j] = color
            for x,y in directions:
                dfs(i +x, j + y, visited)
            
        
        orig_color = image[sr][sc]
        dfs(sr, sc, set())
        return image
        # for i in range(len(image)):
        #     for j in range(len(image[0])):
        #         if image[i][j] == orig_color:
        #             dfs(i, j)
        