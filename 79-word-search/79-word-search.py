class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(board, i, j, visited, k):
            
            if k >= len(word):
                return True
           
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in visited:
                return False

            
            if board[i][j] == word[k]:
                for x,y in directions:
                    visited.add((i, j))
                    if dfs(board, i+x, j+y, visited, k+1):
                        return True
                visited.remove((i, j))
            return False  
   
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, i, j, set(), 0):
                        return True
                    
        return False
                    
                    
                    
        