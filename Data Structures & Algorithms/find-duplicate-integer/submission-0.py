class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sort=sorted(nums)
        for i in range (0,len(sort)-1):
            if sort[i]==sort[i+1]:
                return sort[i]
        return 


        