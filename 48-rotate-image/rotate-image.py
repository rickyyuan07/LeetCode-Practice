class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            r1, r2 = i, n-i-1
            c1, c2 = i, n-i-1
            for j in range(n-1-2*i):
                matrix[r1+j][c2], matrix[r1][c1+j] = matrix[r1][c1+j], matrix[r1+j][c2]
                matrix[r2-j][c1], matrix[r1][c1+j] = matrix[r1][c1+j], matrix[r2-j][c1]
                matrix[r2][c2-j], matrix[r2-j][c1] = matrix[r2-j][c1], matrix[r2][c2-j]

        return