class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range (0,len(nums)-1):
            if nums[i]>nums[i+1]:
                return nums[i+1]
        return nums[0]
        
        #now we can walk thoruth right array and do binary search 
        #one thing to consider what happens if the whole thing is sorted 

        