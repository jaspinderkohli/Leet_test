class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0   

        max_profit = curr_price = 0
        for price in prices[::-1]:
            curr_price = max(curr_price, price)
            max_profit = max(max_profit, curr_price - price)
        return max_profit
