class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        for num in nums:
            result=result^num
           
        return result






        