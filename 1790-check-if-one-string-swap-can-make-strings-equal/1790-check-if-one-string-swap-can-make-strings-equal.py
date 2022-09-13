class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        
        if sorted(s1) != sorted(s2):
            return False
        
        counter = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
        return counter == 2 or counter == 0       
          
        
#         for i in list(difference1):
#             if i not in difference2:
#                 return False

#         return counter == 2 and len(difference1) == 2 and len(difference2) == 2
            
        