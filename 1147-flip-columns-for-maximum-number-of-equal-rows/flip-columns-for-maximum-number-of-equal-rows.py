class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dd = Counter()
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            ll = []
            for i in range(n):
                if not row[i]:
                    ll.append(i)
            
            dd[tuple(ll)] += 1
        
        ans = 0
        for met, value in dd.items():
            # Construct negating of met
            met2 = sorted(set(range(n)) - set(met))
            ans = max(ans, value + dd[tuple(met2)])

        return ans