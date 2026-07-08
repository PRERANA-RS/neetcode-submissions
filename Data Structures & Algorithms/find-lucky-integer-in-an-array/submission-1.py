class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        luck=-1
        for num in arr:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for key,val in d.items():
            if key==val and luck<key:
                luck=key

        return luck
                

        

        
        