class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0] * (n+1) for _ in range(m+1)]
        grid[1][1] = 1 if obstacleGrid[0][0] == 0 else 0
        # obstacleGrid[i][j] corresponds to grid[i+1][j+1]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                grid[i+1][j+1] += grid[i][j+1] + grid[i+1][j]

        return grid[i+1][j+1]