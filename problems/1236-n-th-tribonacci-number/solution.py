class Solution:
    def tribonacci(self, n: int) -> int:
        i = 3
        if n == 0:
            return 0
        elif n < 3:
            return 1

        dp = [None] * (n+1)
        dp[0] = 0
        dp[1] = 1 
        dp[2] = 1 
        while i <= n:
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
            i+=1
        return dp[n]
        
