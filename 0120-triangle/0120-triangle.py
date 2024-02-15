class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def tri(i,j,dp):
            if i == n - 1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            down = triangle[i][j] + tri(i+1,j,dp)
            diag = triangle[i][j] + tri(i+1,j+1,dp)
            dp[i][j] = min(down,diag)
            return dp[i][j]
        
        n = len(triangle)
        dp = [[-1 for i in range(n) ]for j in range(n)]
        return tri(0,0,dp)
        