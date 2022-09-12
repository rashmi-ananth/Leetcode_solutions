class Solution:
    def reverse(self, x: int) -> int:
        
        
        # check if negative
        check = False
        if x < 0:
            check = True

        
        new_int = 0
        factor = 10
        x = abs(x)
        find_nonzero = False
        
        while x > 0:
            right = x % 10
            if right == 0 and not find_nonzero:
                x //= 10
                continue
            find_nonzero = True
            new_int = (new_int * factor) + right
            x //= 10

        if check:
            new_int = -new_int
        
        if new_int > (2**31 - 1) or new_int < -2**31:
            return 0
        
        return new_int

    
    
        