class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        
        first = 1
        second = 2
        temp = second
        
        # num of ways to reach top = sum of two prev step counts
        for i in range(2, n):
            temp = first + second
            first = second
            second = temp
            
        return temp
        
        

        