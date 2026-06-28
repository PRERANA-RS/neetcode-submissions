class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        
        while i<=j:
            mid=(i+j)//2
            if target >nums[mid]:
                i=i+1
            if target< nums[mid]:
                j=j-1
            if target==nums[mid]:
                return mid
        return -1


        