class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=sorted(nums)
        for i in range (0,len(nums)):
            if i ^ a[i]:
                return i
        return i+1
        