class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        sell=0
        s=0
        b=0
        profit=0
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
                sell=prices[i]
                b=i
            elif sell<prices[i]:
                sell=prices[i]
                s=i
            if profit<sell-buy and s>b:
                profit= sell-buy

        return profit
