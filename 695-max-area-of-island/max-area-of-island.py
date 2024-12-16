class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        ans = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1 or visited[i][j]:
                return 0
            area = 1
            visited[i][j] = True
            
            dx = [1, 0, -1, 0]
            dy = [0, -1, 0, 1]
            for k in range(4):
                area += dfs(i+dx[k], j+dy[k])
            
            return area
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = dfs(i, j)
                    ans = max(ans, area)
                
        return ans