class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        lst = sorted(costs, key=lambda x: x[0]-x[1])
        
        print(lst)
        
        total = 0
        for i in range(len(lst)//2):
            total += lst[i][0]
         
        for i in range(len(lst)//2, len(lst)):
            total += lst[i][1]
            
        return total
            
        
        
     
    