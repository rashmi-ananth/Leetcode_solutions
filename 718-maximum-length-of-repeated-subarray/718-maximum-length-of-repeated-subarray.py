class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
   
        matrix = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        # for i in range(len(nums1) + 1):
        #     matrix.append(lst)
           
        # print(matrix)
        
        # print(matrix2)
        
        for i in range(len(nums1) -1, -1, -1):
            for j in range(len(nums2) -1, -1, -1):
                if nums1[i] == nums2[j]:
                    matrix[i][j] += matrix[i+1][j+1] + 1
                    
        max_v = 0
        for i in range(len(matrix)):
            max_v = max(max_v, max(matrix[i])) 
        return max_v
    
    
    
    