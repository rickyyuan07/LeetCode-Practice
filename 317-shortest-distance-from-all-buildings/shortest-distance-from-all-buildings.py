class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        k = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    k.append((i, j))

        shortest_paths = [[[-1] * m for _ in range(n)] for _ in range(len(k))]
        
        for i, (x, y) in enumerate(k):
            # Run BFS to find the shortest path
            queue = deque([(x, y, 0)])  # (x, y, dist)
            shortest_paths[i][x][y] = 0
            while queue:
                curx, cury, dist = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = curx+dx, cury+dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and shortest_paths[i][nx][ny] == -1:
                        shortest_paths[i][nx][ny] = dist + 1
                        queue.append((nx, ny, dist+1))

        ans = (-1, -1)
        MAX = 99999999
        min_dist = MAX
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue
                dist = 0
                valid = True
                for kk in range(len(k)):
                    if shortest_paths[kk][i][j] == -1:
                        valid = False
                        break
                    dist += shortest_paths[kk][i][j]
                
                if valid and dist < min_dist:
                    min_dist = dist
                    ans = (i, j)

        if min_dist == MAX:
            return -1
        return min_dist
