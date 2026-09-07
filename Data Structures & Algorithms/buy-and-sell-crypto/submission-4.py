class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    sub= prices[j]-prices[i]
                    maxp= max(maxp, sub)
        return maxp



        
            

                
        



        