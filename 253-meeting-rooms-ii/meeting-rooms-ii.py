class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort by the the intervals' start time
        intervals.sort()

        pq = []
        heapq.heapify(pq)  # min heap storing (end, start)
        ans = -1
        for itv in intervals:
            s, e = itv
            heapq.heappush(pq, (e, s))
            if pq and pq[0][0] <= s:
                heapq.heappop(pq)
            
            ans = max(ans, len(pq))
        
        return ans