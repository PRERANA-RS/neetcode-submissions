class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lp=len(nums)-1
        triplet=[]
        for i in range(0,len(nums)):
            lp = len(nums) - 1  # ✅ resets every iteration of i
            sp = i + 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while sp<lp:
                if nums[sp] + nums[lp] + nums[i] == 0:
                    triplet.append([nums[i], nums[sp], nums[lp]])
                    sp = sp + 1
                    lp = lp - 1
                    while sp < lp and nums[sp] == nums[sp-1]:  # skip sp duplicates
                        sp += 1
                    while sp < lp and nums[lp] == nums[lp+1]:  # skip lp duplicates
                        lp -= 1

                elif nums[sp]+nums[lp]+nums[i]>0:
                    lp=lp-1
                else:
                    sp=sp+1
        return triplet 

        