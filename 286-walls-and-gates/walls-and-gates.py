class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        n, m = len(rooms), len(rooms[0])

        queue = deque()

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        dd = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        while queue:
            i, j = queue.popleft()
            for di, dj in dd:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= m or rooms[ni][nj] != INF:
                    continue
                rooms[ni][nj] = rooms[i][j] + 1
                queue.append((ni, nj))