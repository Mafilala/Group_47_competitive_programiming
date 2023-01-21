class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        z_r = []
        z_c = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    z_r.append(i)
                    z_c.append(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in z_r:
                    matrix[i] = [0] * len(matrix[0])
                    break
                elif j in z_c:
                    matrix[i][j] = 0
