class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter={}
        count=0
        if len(s)!=len(t):
            return False
        for char in s:
            letter[char]=letter.get(char,0)+1
        for char in t:
            letter[char]=letter.get(char,0)-1
        anagram= all(value==0 for value in letter.values())
        if anagram:
            return True
        return False

            
        