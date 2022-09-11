class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lst = list(range(1,n+1))
        counter = n
        idx = 0
        
        while counter > 1:
            idx += k - 1
            if idx > n - 1:
                idx = (idx % n)
                
            lst.remove(lst[idx])
            counter -= 1
            n = counter
            
            
        
        return lst[0]
        
        
            
        
        
        
        
#         [None,None,3,None,5]
        5
        
        
        

        