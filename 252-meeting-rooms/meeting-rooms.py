class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n == 0:
            return True
        intervals.sort()

        interval = intervals[0]
        for i in range(1, n):
            cur = intervals[i]
            if cur[0] < interval[1]:
                return False
            interval[1] = max(interval[1], cur[1])
        return True