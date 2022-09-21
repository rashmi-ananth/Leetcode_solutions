class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        sorted_costs = sorted(costs, key=lambda x:(x[0]-x[1]))
        
        total = 0
        for i in range(len(costs) // 2):
            total += sorted_costs[i][0]
        
   
        for j in range(i+1, len(costs)):
            total += sorted_costs[j][1]
  
        return total
     
    