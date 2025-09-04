class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        i = 0
        while i < n:
            j = i
            while j+1 < n and prices[j] <= prices[j+1]:
                j += 1
            
            ans += prices[j] - prices[i]
            i = j+1
        
        return ans
