class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col = False
        row = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                row = True
                break
                
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col = True
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0


        if row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col:
            for j in range(len(matrix)):
                matrix[j][0] = 0
            
                    
        
  
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         zero_rows = set()
#         zero_cols = set()
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
                
#                 if matrix[i][j] == 0:
#                     zero_rows.add(i)
#                     zero_cols.add(j)
                    
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if i in zero_rows or j in zero_cols:
#                     matrix[i][j] = 0
                
                
        
        