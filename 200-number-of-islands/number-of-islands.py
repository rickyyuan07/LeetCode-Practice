class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        ans = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            
            dx = [1, 0, -1, 0]
            dy = [0, -1, 0, 1]
            for k in range(4):
                dfs(i+dx[k], j+dy[k])
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    ans += 1
                    dfs(i, j)
                
        return ans