class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)

        # We find the smallest righti to form the solution
        pq = []  # Priority Queue that stores the (righti, chain_length)
        ans = 0  # Record the current max_length considering all the pairs with righti smaller than current leftj
        for pair in pairs:
            left, right = pair
            while pq and pq[0][0] < left:
                ri, cl = heapq.heappop(pq)
                ans = max(ans, cl)
            
            heapq.heappush(pq, (right, ans + 1))
        
        while pq:
            ri, cl = heapq.heappop(pq)
            ans = max(ans, cl)

        return ans

