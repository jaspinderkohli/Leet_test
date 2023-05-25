class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # Bottom-up
        '''
            Build an array dp where dp[i] is the minimum cost to climb to the top starting from the ith staircase.
        '''

        dp = len(cost)*[0]
        dp[0]=cost[0]
        dp[1] = cost[1]


        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])

