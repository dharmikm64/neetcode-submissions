class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maximum = 0 


        for i in range(1, len(prices)):

            if prices[i] > prices[l]:
                maximum = max(maximum, prices[i] - prices[l])
            else: 
                l = i 
        return maximum 