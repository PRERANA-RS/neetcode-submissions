class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1

        r=max(piles)
        totalhrs=0
        
        while(l<=r):
            mid=(l+r)//2

            for pile in piles:
                totalhrs += math.ceil(pile/mid)
            
            if totalhrs<=h :
                r=mid-1
            else:
                l=mid+1
            totalhrs=0
        return l
             

            


        