class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        
        num_steps = [0] * n
        num_steps[0] = 1
        num_steps[1] = 2
        
        # num of ways to reach top = sum of two prev step counts
        for i in range(2, n):
            num_steps[i] = num_steps[i-1] + num_steps[i-2]
            
        return num_steps[-1]
        
        

        