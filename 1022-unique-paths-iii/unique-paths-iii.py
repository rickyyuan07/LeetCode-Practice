class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        need = 0 # value not -1
        sx, sy = -1, -1

        for i in range(m):
            for j in range(n):
                need += 1 if grid[i][j] != -1 else 0
                if grid[i][j] == 1:
                    sx, sy = i, j

        self.ans = 0

        def dfs(x, y, visited):
            if grid[x][y] == 2:
                if visited == need:
                    self.ans += 1
                return
        
            tmp = grid[x][y] # retain the original value
            grid[x][y] = -1

            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    dfs(nx, ny, visited + 1) 

            grid[x][y] = tmp
        
        dfs(sx, sy, 1)
        return self.ans
        