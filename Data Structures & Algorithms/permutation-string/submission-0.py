class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic={}
        substring={}
        k=0
        i=0
        for char in s1:
            dic[char]=dic.get(char,0)+1
        for j in range(0,len(s2)):#range (0,len(s1)):
            while i<len(s1) and k<len(s2):
                substring[s2[k]]=substring.get(s2[k],0)+1
                k+=1
                i=i+1
            #print(substring)
            #print(dic)
            if substring == dic:
                return True
            k=j
            i=0
            substring={}
        return False

        


