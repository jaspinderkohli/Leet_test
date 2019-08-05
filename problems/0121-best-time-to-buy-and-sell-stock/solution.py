class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """            
        if not prices:
            return 0   

        max_profit = sell_price = 0
        for price in prices[::-1]:
            sell_price = max(sell_price, price)
            max_profit = max(max_profit, sell_price - price)
        return max_profit
        
