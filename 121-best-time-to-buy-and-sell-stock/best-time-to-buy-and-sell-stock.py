class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        future_max_list = [0] * n
        max_price = -1
        for i in range(n):
            max_price = max(max_price, prices[n-1-i])
            future_max_list[n-1-i] = max_price
        
        ans = 0
        for i in range(n-1):
            ans = max(ans, future_max_list[i+1] - prices[i])
        
        return ans