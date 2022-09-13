class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        
        counter = 0
        difference1 = set()
        difference2 = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                difference1.add(s1[i])
                difference2.add(s2[i])
                counter += 1
                
          
        for i in list(difference1):
            if i not in difference2:
                return False

        return counter == 2 and len(difference1) == 2 and len(difference2) == 2
            
        