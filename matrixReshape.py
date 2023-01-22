class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        ans = [[] for i in range(r)]
        for i in range(m):
            for j in range(n):
                val = mat[i][j]
                idx = (i * n) + j
                ans[idx // c].append(val)
        return ans
