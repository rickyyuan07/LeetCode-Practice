class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dindex = {}
        for i, x in enumerate(nums):
            if target - x in dindex:
                return dindex[target-x], i
            else:
                dindex[x] = i
        
        return 0, 0