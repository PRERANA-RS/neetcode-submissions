class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps=temperatures
        n=len(temperatures)
        stk=[]
        result=n*[0]
        for i,t in enumerate(temps):
            while stk and stk[-1][0]<t:
                stk_t,stk_i = stk.pop()
                result[stk_i]=i-stk_i

            stk.append((t,i))
        return result
