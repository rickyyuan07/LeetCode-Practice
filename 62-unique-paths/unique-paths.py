class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * (n+1)] * (m+1)
        grid[1][1] = 1
        print(grid)
        for i in range(m):
            for j in range(n):
                grid[i+1][j+1] = grid[i][j+1] + grid[i+1][j]

        return grid[i+1][j+1]