class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = None
        ans = 0
        for intv in intervals:
            # Not overlapping, update prev
            if not prev or intv[0] >= prev[1]:
                prev = intv
            else:
                prev[1] = min(prev[1], intv[1])
                ans += 1
        
        return ans