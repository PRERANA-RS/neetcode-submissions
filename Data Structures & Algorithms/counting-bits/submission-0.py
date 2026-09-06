class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[0]
        bits=0
        for i in range(1,n+1):
            while(i!=0):
                if i&1:
                    bits+=1
                i>>=1

                

          
                
            a.append(bits)
            bits=0
        return a

        