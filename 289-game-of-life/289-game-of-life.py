class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#         < 2 dies
#         2-3 lives
#         > 3 dies
        
#         3 live bute dead: live
            
#             0-1: -2
#             1-0: -1



        for i in range(len(board)):
            for j in range(len(board[0])):
                alive_n = 0
                dead_n = 0
                
                # i > 0 j > 0
#                 i < len(board) -1 j < len(board[0]) - 1
                
                if i < len(board) - 1:
                    val = board[i+1][j]
                    if val == 0 or val == -2:
                        dead_n += 1
                    if val == 1 or val == -1:
                        alive_n += 1
                if i > 0:
                    val = board[i-1][j]
                    if val == 0 or val == -2:
                        dead_n += 1
                    if val == 1 or val == -1:
                        alive_n += 1
                if j < len(board[0]) - 1:
                    val = board[i][j+1]
                    if val == 0 or val == -2:
                        dead_n += 1
                    if val == 1 or val == -1:
                        alive_n += 1
                if j > 0:
                    val = board[i][j-1]
                    if val == 0 or val == -2:
                        dead_n += 1
                    if val == 1 or val == -1:
                        alive_n += 1
                if i < len(board) - 1 and j < len(board[0]) - 1:
                    val = board[i+1][j+1]
                    if val == 0 or val == -2:
                        dead_n += 1
                    if val == 1 or val == -1:
                        alive_n += 1
                if i > 0 and j > 0:
                    val = board[i-1][j-1]
                    if val == 0 or val == -2:
                        dead_n += 1
                    if val == 1 or val == -1:
                        alive_n += 1
                if i < len(board) - 1 and j > 0:
                    val = board[i+1][j-1]
                    if val == 0 or val == -2:
                        dead_n += 1
                    if val == 1 or val == -1:
                        alive_n += 1
                if i > 0 and j < len(board[0]) - 1:
                    val = board[i-1][j+1]
                    if val == 0 or val == -2:
                        dead_n += 1
                    if val == 1 or val == -1:
                        alive_n += 1
                curr_val = board[i][j]
                if curr_val == 1:
                    if alive_n < 2 or alive_n > 3:
                        board[i][j] = -1
                    if alive_n == 2 or alive_n == 3:
                        board[i][j] = 1
                if curr_val == 0:
                    if alive_n == 3:
                        board[i][j] = -2
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == -2:
                    board[i][j] = 1
                
                    
                
#                 i+1, j
#                 i-1, j
#                 i, j+1
#                 i, j-1
                
#                 i+1, j+1
#                 i-1, j-1
#                 i+1, j-1
#                 i-1, j+1
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        
        