class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        diff = []
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
            
        if not diff:
            return True
        
        if len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]:
            return True
        
        return False