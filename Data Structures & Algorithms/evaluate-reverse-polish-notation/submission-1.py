class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        total=0
        for value in tokens:
            if value not in ['+','-','*','/']:
                stk.append(int(value))
            elif len(stk)>1:
                op1=stk.pop()
                op2=stk.pop()
                if value == '-':
                    total=op2-op1
                elif value == '+':
                    total=op1+op2
                elif value == '*':
                    total=op1*op2
                else:
                    total=int(op2/op1)
                stk.append(total)
                
        return stk.pop()
            


        