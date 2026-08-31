class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        for r in range(len(prices)):
            while(r < len(prices)):
                if(prices[l] > prices[r]):
                    r += 1
                    continue
                else:
                    maxProfit = max(maxProfit, prices[r] - prices[l])
                    r += 1
            l += 1
        return maxProfit