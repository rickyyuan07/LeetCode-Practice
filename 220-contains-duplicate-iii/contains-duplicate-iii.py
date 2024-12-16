from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # sliding window
        s = SortedList()
        for i, num in enumerate(nums):
            if i > indexDiff:
                s.remove(nums[i-indexDiff-1])
            pos1 = s.bisect_left(num - valueDiff)
            pos2 = s.bisect_right(num + valueDiff)
            if pos1 != pos2:
                return True
            s.add(num)
        
        return False