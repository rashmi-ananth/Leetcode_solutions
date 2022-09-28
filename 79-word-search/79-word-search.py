class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row, col = len(board), len(board[0])
        path = set()
        s = ''
        for r in range(row):
            for c in range(col):
                s += board[r][c]
        for w in word:
            if w not in s:
                return False
            
            
            
        def dfs(i, j, idx):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[idx] or (i, j) in path:
                return False
            
            if idx >= len(word) - 1:
                return True
            
            path.add((i,j))
            result = dfs(i+1, j, idx + 1) or dfs(i-1, j, idx + 1) or dfs(i, j+1, idx + 1) or dfs(i, j-1, idx + 1)
            
            path.remove((i,j))
            return result
            
      
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
    