class Solution:
    def countElements(self, arr: List[int]) -> int:
        C = Counter(arr)
        ans = 0
        for x, y in C.items():
            ans += (x+1 in C) * y
        return ans