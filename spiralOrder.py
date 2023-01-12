class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        ans = []
        while (l < r) and (t < b):
        # left to right
            for i in range(l, r):
                ans.append(matrix[t][i])
            t += 1
        # top to buttom
            for i in range(t, b):
                ans.append(matrix[i][r - 1])
            r -= 1
            if not (l < r and t < b):
                break
        # right to left
            for i in range(r - 1, l - 1, -1):
                ans.append(matrix[b - 1][i])
            b -= 1
        # buttom to top
            for i in range(b - 1, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
        return ans
                
