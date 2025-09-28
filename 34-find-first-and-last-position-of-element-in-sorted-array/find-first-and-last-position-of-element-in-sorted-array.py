class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        if n == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]
        l, r = 0, n
        # Find left
        while l < r:
            m = (l+r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m+1
        
        left_idx = l
        if left_idx == n or nums[left_idx] != target:
            return [-1, -1]


        l, r = 0, n
        # Find right
        while l < r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m+1

        right_idx = l
        return [left_idx, right_idx-1]