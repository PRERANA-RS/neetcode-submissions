class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        ftemp=temperatures[0]
        count=0
        for i in range(0,len(temperatures)):
            for j in range(i,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    count=j-i
                    
                    result.append(count)
                    break
                if temperatures[i]>=temperatures[j] and j== len(temperatures)-1:
                    count=0
                    result.append(count)
            

            
            
        return result