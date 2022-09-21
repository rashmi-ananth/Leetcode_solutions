class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
      
    
#     O(2N)  = O(N)


        char_stack = []
        count_stack = []
        
        for i in range(len(s)):
            
            # adding to stacks
            if len(char_stack) > 0 and s[i] ==  char_stack[-1]:
                count_stack[-1] += 1
            else:
                count_stack.append(1)
            char_stack.append(s[i])
            
            # if k duplicates
            if count_stack[-1] == k:
                count_stack.pop()
                for j in range(k):
                    char_stack.pop()
                
        return ''.join(char_stack)
            
            
            
            
            
        
        
    
    