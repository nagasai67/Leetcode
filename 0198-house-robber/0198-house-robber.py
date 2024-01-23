class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        for i in range(len(nums)):
            take = nums[i]
            if i > 1:
                take += dp[i - 2]
            not_take = dp[i - 1]
            dp[i] = max(take,not_take)
        return dp[len(nums) - 1]
        