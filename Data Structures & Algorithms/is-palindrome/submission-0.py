class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        
        s=re.sub(r'[^\w]','',s) 
        s=s.strip(" ")
        j=len(s)-1
        for i in range (0,len(s)):
            
            if s[i] == s[j] :
                
                print(s[i],s[j])
                j=j-1
                continue
            else:
                return False
            
            

            
            
            
        return True

        