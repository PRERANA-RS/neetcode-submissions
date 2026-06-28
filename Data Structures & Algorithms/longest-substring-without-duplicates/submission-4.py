class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        left=0
        max_length=0
        for right in range(0,len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            max_length=max(max_length, right-left+1)
            #print(max_length)




        return max_length

        

