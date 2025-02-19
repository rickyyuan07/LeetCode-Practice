from typing import List

class Solution:
    def dfs(self, i, j, grid, n, m, base_i, base_j, shape):
        # If out of bounds or water, return
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
            return
        
        # Mark as visited
        grid[i][j] = 0

        # Record the relative position of each island cell
        shape.append((i - base_i, j - base_j))

        # Explore all 4 directions
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions:
            self.dfs(i + dx, j + dy, grid, n, m, base_i, base_j, shape)

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        unique_shapes = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    shape = []
                    self.dfs(i, j, grid, n, m, i, j, shape)
                    unique_shapes.add(tuple(shape))  # Convert to tuple to store in set

        return len(unique_shapes)
