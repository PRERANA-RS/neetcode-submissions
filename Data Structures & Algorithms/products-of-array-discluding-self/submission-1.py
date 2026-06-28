class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        prefix=1
        postfix=1
        for i in range (len(nums)):
            result.append(prefix)
            prefix=prefix*nums[i]
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= postfix       # Multiply prefix by accumulated postfix
            postfix = postfix * nums[j] # Update postfix with current number
            
        return result
