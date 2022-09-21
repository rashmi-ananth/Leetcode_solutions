
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        [1,2,3,4,5]
        lst = list(range(1,n+1))
        idx = 0
        while len(lst) > 1:
            idx = (idx + k-1) % len(lst) 
            lst.pop(idx)
        
        return lst[0]

            
            
            
        

    
        

        