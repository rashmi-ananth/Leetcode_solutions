class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)-1,-1, -1):
            if s[i] == ")" or 	 s[i] == ']' or s[i] == "}":
                stack.append(s[i])
            if len(stack) == 0:
                return False
            if s[i] == '(':
                val = stack.pop()
                if val != ")":
                    return False
            if s[i] == '[':
                val = stack.pop()
                if val != "]":
                    return False
            if s[i] == '{':
                val = stack.pop()
                if val != "}":
                    return False
        return len(stack) == 0