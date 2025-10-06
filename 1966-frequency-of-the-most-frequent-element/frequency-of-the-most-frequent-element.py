class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # [1, 4, 8, 13]
        nums.sort()
        n = len(nums)

        left = 0
        window_sum = 0
        ans = 0
        for i, x in enumerate(nums):
            # Treat x as the target
            window_sum += x
            used_k = (i-left+1) * x - window_sum
            while left < i and used_k > k:
                window_sum -= nums[left]
                left += 1
                used_k = (i-left+1) * x - window_sum
            
            window_len = i - left + 1
            ans = max(ans, window_len)
        
        return ans
