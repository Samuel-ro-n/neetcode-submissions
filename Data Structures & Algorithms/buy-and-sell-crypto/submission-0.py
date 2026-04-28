class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=[]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    sub= prices[j]-prices[i]
                    res.append(sub)
        if res:
            return max(res)
        else:
            return 0


        