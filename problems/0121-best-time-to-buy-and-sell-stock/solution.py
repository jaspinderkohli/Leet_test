class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        
        min_price = prices[0]
        max_profit = 0

        for current_time in range(1, len(prices)):
            current_price = prices[current_time]

            min_price = min(min_price, current_price)

            max_profit = max(max_profit, current_price - min_price)

        return max_profit
