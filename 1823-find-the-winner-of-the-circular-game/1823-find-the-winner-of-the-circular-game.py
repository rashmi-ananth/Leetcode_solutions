
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lst = list(range(1,n+1))
        idx = 0
        while len(lst) > 1:
            idx = (idx + k-1) % len(lst) 
            lst.pop(idx)
        
        return lst[0]

            
            
            
        

    
        

        