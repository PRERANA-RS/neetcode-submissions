class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk=[]
        time=0
        grouped=sorted(zip(position,speed),reverse=True)
        for pos, sp in grouped:
            d=target-pos
            time=d/sp
            if stk and time <= stk[-1]:
                pass
            else:
                stk.append(time)
        return len(stk)

        
