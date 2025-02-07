class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(int)
        colors = Counter()
        ans = []
        for id, color in queries:
            prev_color = balls[id]

            if prev_color == color:
                ans.append(len(colors))
                continue
                
            if prev_color in colors:
                colors[prev_color] -= 1
                if colors[prev_color] == 0:
                    del colors[prev_color]
            
            balls[id] = color
            colors[color] += 1
            ans.append(len(colors))
        return ans