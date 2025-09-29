class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left >= n or nums[left] != target:
            return [-1, -1]
        return [left, right-1]