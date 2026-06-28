class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=int(len(nums)/2)
        while i <=len(nums)/2 and j<len(nums):
            if target == nums[i]: 
                return i
            if target == nums[j]:
                return j
            j=j+1
            i=i+1
        return -1
            
        