class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for r in range(1,len(prices)):
            max_profit = max(max_profit,prices[r]-buy)
            buy = min(buy,prices[r])

        return max_profit


        