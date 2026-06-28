class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        if len(s) % 2 != 0: 
            return False

        for char in s:
           
          
            if char == '(' or char =='{' or char == '[' :
                stack.append(char)
            elif not stack:
                return False

            elif (char == '}' and stack[-1] == '{') or (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False 

        
