class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_n = len(p)
        n = len(s)
        tar = Counter(p)

        ans = []
        cur = Counter()
        for i, c in enumerate(s):
            if i >= window_n and s[i-window_n] in tar:
                cur[s[i-window_n]] -= 1
            
            if c in tar:
                cur[c] += 1
                if tar == cur:
                    ans.append(i-window_n+1)


        return ans
            