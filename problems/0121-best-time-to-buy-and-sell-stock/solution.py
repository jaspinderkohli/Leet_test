class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0 

        # We'll greedily update min_price and max_profit, so we initialize
        # them to the first price and the first possible profit
        min_price  = prices[0]
        max_profit = 0

        # Start at the second (index 1) time
        # We can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # If we started at index 0, we'd try to buy *and* sell at time 0.
        # This would give a profit of 0, which is a problem if our
        # max_profit is supposed to be *negative*--we'd return 0.
        for current_time in range(1, len(prices)):
            current_price = prices[current_time]

            # See what our profit would be if we bought at the
            # min price and sold at the current price
            potential_profit = current_price - min_price

            # Update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

            # Update min_price so it's always
            # the lowest price we've seen so far
            min_price  = min(min_price, current_price)

        return max_profit
