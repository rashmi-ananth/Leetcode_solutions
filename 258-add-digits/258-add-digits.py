class Solution:
    def addDigits(self, num: int) -> int:
        
        stack = []
        # print(38 % 10)
        
        while num != 0:
            stack.append(num % 10)
            num = num // 10
        
        total = 0
        while stack:
            num += stack.pop()
            if len(stack) == 0 and num > 9:
                while num != 0:
                    stack.append(num % 10)
                    num = num // 10
                    

        return num
            
        
        
        