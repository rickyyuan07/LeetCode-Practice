class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = [0] * (n+1)  # 0: not colored, 1: white, -1: black
        def dfs(a, c):
            if color[a] != 0:
                if color[a] != c:
                    return False
                else:
                    return True
            color[a] = c
            for b in graph[a]:
                if color[b] == color[a] or not dfs(b, -c):
                    return False
                
            return True


        for a, b in dislikes:
            if color[a] != 0 and color[b] != 0:
                continue

            if not dfs(a, 1):
                return False
        
        return True