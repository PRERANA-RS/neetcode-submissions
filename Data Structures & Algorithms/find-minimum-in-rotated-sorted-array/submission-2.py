class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid=len(nums)//2
        mini=nums[mid]
        right=len(nums)-1
        left=0
        while left<right:
            
                
            if nums[mid]>nums[right] :
                left=mid+1
            else:
                right=mid
            mid=(left+right)//2
        return nums[left]
            



        