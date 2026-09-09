class Solution:
    def reverse(self, x: int) -> int:
        num=x
        
        res=0
        if x<0:
            x=-1*x
        
        while x>0:
            n=x%10
            res=res*10+n
            x=x//10
        if num<0:
            res=res*-1

        if res > 2**31 - 1 or res < -2**31:
            return 0
        
        return int(res)


        