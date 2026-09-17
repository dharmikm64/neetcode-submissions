class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1 
        maximum = 0

        for i in range(len(prices) - 1):
            if prices[l] < prices[r]:
                maximum = max(maximum, prices[r] - prices[l])
            else: 
                l = r 
            r += 1
        return maximum 
