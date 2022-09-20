class Solution:
    def minDays(self, n: int) -> int:
        
        
        def backtrack(n):
            
            if n == 1:
                memo[1] = 1
                return 1
            if n == 2:
                memo[2] = 2
                return 2
            if n == 3:
                memo[3] = 2
                return 2
            
            if n in memo.keys():
                return memo[n]
            
            
            
            memo[n] = 1 + min((n%2) + backtrack(n//2), (n%3) + backtrack(n//3))
            return memo[n]
            
            
            
        memo = dict()
        backtrack(n)
        
        return memo[n]
        
        
        

            