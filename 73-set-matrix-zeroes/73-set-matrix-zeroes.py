class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#         1   0   1
#         1   0   1
#         1   1   1
        
#         0   0   0
#         0   0   0
#         1   0   1


        # check if first row/col has any zeros
        col_check = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_check = True
                break
        row_check = False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                row_check = True
                break   
       
    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
   
        
        # update first row/col
        if col_check:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if row_check:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

    
    
    
    
    
    
    
    
    
    
    
    
        

        
        