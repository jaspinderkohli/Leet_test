class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize the minimum price seen so far and the maximum profit seen so far to 0
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # update the minimum price seen so far
            min_price = min(min_price, price)

            # calculate the potential profit if the stock is sold at the current price
            profit = price - min_price

            # update the maximum profit seen so far if the current potential profit is larger than the current maximum profit
            max_profit = max(max_profit, profit)

        return max_profit
