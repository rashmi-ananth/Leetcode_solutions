class Solution:
    def decodeString(self, s: str) -> str:
        
        
        # Time: O(maxk * N)
        # Space: O(n)
        

        
        stack = []
        i = 0
        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
                i += 1
                continue
            
            string_lst = []
            char = 'a'
            while char.isalpha():
                char = stack.pop()
                if char.isalpha():
                    string_lst.append(char)
                
            string_lst = string_lst[::-1]
            string = ''.join(string_lst)
            
            integer = 0
            factor = 1
            while True:
                if stack and stack[-1].isdigit():
                    integer += factor * int(stack.pop())
                    factor *= 10
                else:
                    break
                
            final_str = integer * string
            stack.append(final_str)
            i += 1

            
        return ''.join(stack)
            
         
         
         
         
         
            
            
        
        
       
        