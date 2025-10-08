class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points: # O(nlogn)
            x, y = point
            dis = x*x + y*y
            heapq.heappush(pq, (dis, x, y))

        ans = []
        for _ in range(k): # O(klogn)
            dis, x, y = heapq.heappop(pq)
            ans.append([x,y])
        
        return ans