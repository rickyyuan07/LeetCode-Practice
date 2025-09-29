class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def explore(sx, sy, x, y, visited):  # return list of offsets
            ret = [(x-sx, y-sy)]
            visited[x][y] = True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                    offset = explore(sx, sy, nx, ny, visited)
                    ret.extend(offset)

            return ret
                
        def canical_form(shape):  # create 4 rotation * 2 reflection = 8 form and select the min as canical form
            def normalize(coords):
                minx = min(x for x, y in coords)
                miny = min(y for x, y in coords)
                return tuple(sorted((x - minx, y - miny) for x, y in coords))

            transforms = []
            for x, y in shape:
                transforms.append([
                    ( x,  y), ( x, -y), (-x,  y), (-x, -y),
                    ( y,  x), ( y, -x), (-y,  x), (-y, -x)
                ])

            res = []
            for k in range(8):
                coords = [transforms[i][k] for i in range(len(shape))]
                res.append(normalize(coords))
            return min(res)


        ilds = set()
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    ild = explore(i, j, i, j, visited)
                    ilds.add(canical_form(tuple(ild)))
                    print(canical_form(tuple(ild)))

        return len(ilds)