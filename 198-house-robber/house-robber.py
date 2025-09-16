class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n + 1)]

        for i in range(n):
            dp[i+1][0] = max(dp[i][0], dp[i][1])
            dp[i+1][1] = dp[i][0] + nums[i]

        return max(dp[n][0], dp[n][1])
