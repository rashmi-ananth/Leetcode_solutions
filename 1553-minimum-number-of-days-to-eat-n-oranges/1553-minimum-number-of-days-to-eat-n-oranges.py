class Solution:
    def minDays(self, n: int) -> int:
        
        
        min_days = dict()
        def dfs(n, min_days):
  
            if n == 1:
                return 1
            
            if n == 0:
                return 0
            
            if n in min_days.keys():
                return min_days[n]
            
            min_days[n] = 1 + min(n % 3 + dfs(n//3, min_days), n % 2 + dfs(n//2, min_days))
            
            return min_days[n]
        
        
  
        return dfs(n, min_days)
        
        
        