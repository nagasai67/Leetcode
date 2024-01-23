class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(i):
            if dp[i] != -1:
                return dp[i]
            if i == 0 or i == 1:
                return 1
            dp[i] = climb(i - 1) + climb(i - 2)
            return dp[i]
        dp = [-1] * (n + 1)
        return climb(n)

        