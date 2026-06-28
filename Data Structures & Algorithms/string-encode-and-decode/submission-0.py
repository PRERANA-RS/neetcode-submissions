class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded= ""
        lenght=0
        new=""
        for string in strs:
            length=len(string)
            new=f"{length}#{string}"
            encoded=encoded+new

            

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded=[]
        word=""
        wl=0
        i=0
        while i <len(s):
            if s[i].isdigit():
                wl = wl * 10 + int(s[i])
                i=i+1
            else :
                word=s[i+1:i+1+wl]
                decoded.append(word)
                    
                    
                                    
                i=i+1+wl
                wl=0
            
        return decoded 

            

            

            
