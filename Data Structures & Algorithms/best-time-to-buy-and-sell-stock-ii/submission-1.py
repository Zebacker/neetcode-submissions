class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpr = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]: maxpr += prices[i+1] -prices[i]
            else: i+=1
        return maxpr
