class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

        adj = [[] for i in range(n)]
        print(adj)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(cur, prev):
            visited.add(cur)
            for out_node in adj[cur]:
                if prev == out_node:
                    continue
                if out_node in visited or not dfs(out_node, cur):
                    return False
                
            return True
        
        return dfs(0, -1) and len(visited) == n