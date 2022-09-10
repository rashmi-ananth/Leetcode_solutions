import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        matrix = np.zeros((len(word1) + 1, len(word2) + 1))
        
        for i in range(len(matrix)):
            matrix[i][0] = i
        for i in range(len(matrix[0])):
            matrix[0][i] = i
            
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                    
                else:
                    matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
                    
        return int(matrix[-1][-1])
        
        
        