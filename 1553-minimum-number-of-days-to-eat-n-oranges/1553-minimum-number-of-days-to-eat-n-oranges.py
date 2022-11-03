class Solution:
    def minDays(self, n: int) -> int:
        
        def find_min(n):
            
            if n == 1:
                memo[1] = 1
                return memo[1]
            if n == 2:
                memo[2] = 2
                return memo[2]
            if n == 3:
                memo[3] = 2
                return memo[3]
            
            if n in memo.keys():
                return memo[n]
            
            memo[n] =  1 + min(n%2 + find_min(n//2), n%3 + find_min(n//3))
            return memo[n]
     
        memo = dict()
        find_min(n)
        
        return memo[n]
        
        
        
        
        