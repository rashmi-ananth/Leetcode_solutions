class Solution:
    def decodeString(self, s: str) -> str:
        
        # creating a stack
        # add char to stack
        # if char == ]: pop off all chars until numbers
        # add new (reversed) char to stack and continue
        
        
        stack = []
        i = 0
        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
                i += 1
                continue
            val = stack.pop()
            string = []
            while val != '[':
                string.append(val)
                val = stack.pop()
            
            val2 = stack.pop()
            number = 0
            factor = 1
            while val2.isdigit():
                number += (int(val2) * factor) 
                factor = factor * 10
                if stack and stack[-1].isdigit():
                    val2 = stack.pop()
                else:
                    break
            string.reverse()
            new_string = string * number
            result_string = ''.join(new_string)
            stack.append(result_string)
            i += 1
         
        return ''.join(stack)
 
     
                
            
            
        