class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # BFS on (x, y, r) where x, y is coord and r is the remaining obs can eliminate
        m, n = len(grid), len(grid[0])

        q = deque([(0, 0, k, 0)])
        ans = -1
        visited = [[-1]*n for _ in range(m)]
        visited[0][0] = k
        while q:
            x, y, r, step = q.popleft()
            if x == m-1 and y == n-1:
                ans = step
                break
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and r > visited[nx][ny]:
                    nr = r if grid[nx][ny] == 0 else r-1
                    if nr < 0:
                        continue
                    visited[nx][ny] = nr
                    q.append((nx, ny, nr, step+1))
    
        return ans