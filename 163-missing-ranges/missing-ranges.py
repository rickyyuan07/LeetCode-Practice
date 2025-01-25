class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[lower, upper]]
        ans = []
        if lower < nums[0]:
            ans.append([lower, nums[0]-1])
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                continue
            ans.append([nums[i-1]+1, nums[i]-1])
        
        if upper > nums[-1]:
            ans.append([nums[-1]+1, upper])
        return ans
