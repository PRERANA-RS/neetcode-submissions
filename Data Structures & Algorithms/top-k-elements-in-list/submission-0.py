class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        a=[]
        i=0
        for num in nums:
            d[num]=d.get(num,0)+1
        d=sorted(d, key=d.get, reverse=True)
        return d[:k]