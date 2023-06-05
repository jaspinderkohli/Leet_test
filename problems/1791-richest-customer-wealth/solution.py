class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for wealth in accounts:
            max_wealth = max(sum(wealth),max_wealth)
        return max_wealth

