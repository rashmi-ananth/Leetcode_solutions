class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        start = 0
        counter = 0
        
        for i in range(len(board)):
            for j in range(len(board[i]) - 2):
                val1 = abs(board[i][j])
                val2 = abs(board[i][j + 1])
                val3 = abs(board[i][j + 2])
                if val1 == val2 and val2 == val3 and val3 != 0:
                    counter += 1
                    board[i][j] = -val1
                    board[i][j + 1] = -val1
                    board[i][j + 2] = -val1
         
        for i in range(len(board) - 2):
            for j in range(len(board[i])):
                val1 = abs(board[i][j])
                val2 = abs(board[i + 1][j])
                val3 = abs(board[i + 2][j])
                if val1 == val2 and val2 == val3 and val3 != 0:
                    counter += 1
                    board[i][j] = -val1
                    board[i + 1][j] = -val1
                    board[i + 2][j] = -val1
                    
                    
        for j in range(len(board[0])):
            location = len(board) - 1
            for i in range(len(board) -1, -1, -1):
      
                if board[i][j] > 0:
                    board[location][j] = board[i][j]
                    location -= 1
            while location >= 0:
                board[location][j] = 0
                location -= 1
                
          
        if counter > 0:
            return self.candyCrush(board)  
        return board
        
                
        