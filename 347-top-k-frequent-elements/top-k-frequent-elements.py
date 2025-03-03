class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = []

        for num, cnts in freqs.items():
            heapq.heappush(heap, (cnts, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            result.append(heapq.heappop(heap)[-1])

        return list(reversed(result))
