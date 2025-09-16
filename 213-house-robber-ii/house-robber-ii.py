class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Case 1: not consider the last
        dp1 = [[0,0] for i in range(n)]
        for i in range(n-1):
            dp1[i][0] = max(dp1[i-1])
            dp1[i][1] = dp1[i-1][0] + nums[i]
        
        # Case 2: not consider the first
        dp2 = [[0,0] for i in range(n)]
        for i in range(n-1):
            dp2[i][0] = max(dp2[i-1])
            dp2[i][1] = dp2[i-1][0] + nums[i+1]

        return max(dp1[n-2][0], dp1[n-2][1], dp2[n-2][0], dp2[n-2][1])