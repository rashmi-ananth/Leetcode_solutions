class Solution:
    def decodeString(self, s: str) -> str:
        
        
        # stack to iterate through values
        # if find ']' then pop and get number and entire str
        # add it back to stack
        # join all strings
        
 
        stack = []
        idx = 0
        
        while idx < len(s):
            if s[idx] != ']':
                stack.append(s[idx])
                idx += 1
            else:
                # pop all chars
                char_lst = []
                temp = stack.pop()
                
                while len(temp) > 0 and temp != '[':
                    char_lst.append(temp)
                    temp = stack.pop()
                char_lst.reverse()
                temp_string = ''.join(char_lst)

                # pop all numbers
   
                val = stack.pop()
                integer = 0
                factor = 1
                while val.isnumeric():
                    integer += (factor * int(val))
                    factor *= 10
                    if len(stack) > 0:
                        val = stack.pop()
                    else:
                        break
                if not val.isnumeric():
                    stack.append(val)
                new_string = temp_string * integer

                stack.append(new_string)
                idx += 1
        
        
        return ''.join(stack)
                
                
                
                
            
    
    