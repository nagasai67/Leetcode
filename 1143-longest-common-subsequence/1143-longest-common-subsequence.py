class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def sub(i1,i2,dp):
            if i1 < 0 or i2 < 0:
                return 0
            if dp[i1][i2] != -1:
                return dp[i1][i2]
            if text1[i1] == text2[i2]:
                dp[i1][i2] = 1 + sub(i1 - 1,i2 - 1,dp)
                return dp[i1][i2]
            else:
                dp[i1][i2] = max(sub(i1 - 1, i2, dp),sub(i1,i2 - 1, dp))
            return dp[i1][i2]
            
        dp = [[-1 for j in range(len(text2))] for i in range(len(text1))]
        return sub(len(text1) - 1, len(text2) - 1, dp)
        
        