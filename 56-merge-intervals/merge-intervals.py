class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for itv in intervals:
            if not ans or itv[0] > ans[-1][1]:
                ans.append(itv)
            else:
                ans[-1] = [ans[-1][0], max(itv[1], ans[-1][1])]
        
        return ans