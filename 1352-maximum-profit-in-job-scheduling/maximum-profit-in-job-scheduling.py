class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        schedules = list(zip(startTime, endTime, profit))
        schedules.sort()
        # Priority Queue stored the smallest endTime, value is the maxprofit if we select that job
        pq = []

        # Store the max profit gained with jobs' endTime <= cur job's startTime
        # Push the max achievable profit if we choose this current job
        maxprofit = 0
        for start, end, profit in schedules:
            while pq and pq[0][0] <= start:
                e, prof = heapq.heappop(pq)
                maxprofit = max(maxprofit, prof)
            
            heapq.heappush(pq, (end, maxprofit + profit))
        
        while pq:
            e, prof = heapq.heappop(pq)
            maxprofit = max(maxprofit, prof)

        return maxprofit

