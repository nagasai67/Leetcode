class Solution:
    def minCut(self, s: str) -> int:
        def check(i,j,s):
            txt = s[i:j+1]
            return s[i:j+1] == txt[::-1]

        def part(i):
            if i == len(s):
                return 0
            if dp[i] != -1:
                return dp[i]
            count = 0
            max_cnt = 9999
            for j in range(i,len(s)):
                if check(i,j,s):
                    max_cnt = min(max_cnt,1 + part(j + 1))
            dp[i] = max_cnt
            return dp[i]
        
        dp = [-1] * len(s)
        return part(0) - 1





        