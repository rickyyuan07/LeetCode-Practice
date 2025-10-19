class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        arr.sort(key=lambda x: (x[0], -x[1]))

        yy = [i[1] for i in arr]
        
        dp = []  # dp[x] stores the smallest number of length x
        for y in yy:
            idx = bisect_left(dp, y)
            if idx == len(dp):
                dp.append(y)
            else:
                dp[idx] = y
            
        return len(dp)