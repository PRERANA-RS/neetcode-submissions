class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sp=0
        lp=len(numbers)-1
        while(lp>0 and sp<=len(numbers)):
            if numbers[sp]+numbers[lp]==target:
                return [sp+1,lp+1]
            elif numbers[sp]+numbers[lp]>target:
                lp=lp-1
            else:
                sp=sp+1

        return -1
