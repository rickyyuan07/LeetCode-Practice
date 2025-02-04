class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        cur = nums[0]
        ans = -1
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                ans = max(ans, cur)
                cur = nums[i]
            else:
                cur += nums[i]
        
        return max(ans, cur)