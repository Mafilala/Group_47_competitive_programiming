class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        num_of_diag = m + n - 1
        ans = [ [] for _ in range(num_of_diag)]
        for i in range(m):
            for j in range(n):
                idx = (i + j) % (num_of_diag)
                ans[idx].append(mat[i][j])
        odd = True
        final_ans = []
        for li in ans:
            if odd:
                li.reverse()
            final_ans.extend(li)
            odd = not odd
        return final_ans
