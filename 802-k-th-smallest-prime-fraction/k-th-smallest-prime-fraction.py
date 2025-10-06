class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Similar to merge K sorted array
        # However, we don't need to explicitly form the array, we just need to record the index of each array
        n = len(arr)
        # frac_idx[i] means arr[frac_idx[i]]/arr[i], guarantee that frac_idx[i] < i
        frac_idx = [0] * n

        # Use a pq to store the smallest top element of these arrays
        pq = []
        for i in range(1, n):
            heapq.heappush(pq, (arr[0]/arr[i], i))

        while pq and k > 1:
            frac, idx = heapq.heappop(pq)
            if frac_idx[idx]+1 < idx:
                frac_idx[idx] += 1
                heapq.heappush(pq, (arr[frac_idx[idx]]/arr[idx], idx))
            k -= 1
        
        frac, idx = heapq.heappop(pq)
        return [arr[frac_idx[idx]], arr[idx]]

