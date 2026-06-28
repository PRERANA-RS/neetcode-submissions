class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap={}
        for i in range (0, len(nums)):
            
            difference=target-nums[i]
            if (difference in hashmap) and (hashmap.get(difference)!=i):
                return [hashmap.get(difference),i]
            hashmap[nums[i]]=i