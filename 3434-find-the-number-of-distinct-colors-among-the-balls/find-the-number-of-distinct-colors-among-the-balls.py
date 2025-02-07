class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(int)
        colors = Counter()
        ans = []
        for q in queries:
            colors[balls[q[0]]] -= 1
            if colors[balls[q[0]]] <= 0:
                del colors[balls[q[0]]]
            balls[q[0]] = q[1]
            colors[q[1]] += 1

            ans.append(len(colors))
        return ans