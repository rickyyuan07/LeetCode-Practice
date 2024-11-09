class Solution:
    def alienOrder(self, words: List[str]) -> str:
        edges = defaultdict(list)
        indegree = {}
        for word in words:
            for ch in word:
                indegree[ch] = 0

        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""  # Invalid order as word1 is prefix of word2
            j = 0
            while j < min(len(words[i-1]), len(words[i])):
                ch1, ch2 = words[i-1][j], words[i][j]
                if ch1 != ch2: # we found an edge ch1 -> ch2
                    edges[ch1].append(ch2)
                    indegree[ch2] += 1
                    break
                j += 1
            
        # print(edges)
        # print(indegree)

            # topological sort
        ans = ""
        queue = []
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)
        
        while len(queue) != 0:
            v = queue[0]
            for node in edges[v]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
            
            queue.pop(0)
            ans += v

        if len(ans) != len(indegree):
            return ""
        
        return ans
