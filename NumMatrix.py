class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat_prefix = []
        pseudo = [0] * len(matrix[0])
        self.mat_prefix.append(pseudo)
        for row in matrix:
            new_row = []
            prev = 0
            for idx, val in enumerate(row):
                add = self.mat_prefix[-1][idx]
                new_row.append(val + add + prev)
                prev += val
            new_row.append(0)
            self.mat_prefix.append(new_row)
        self.mat_prefix.pop(0)
        row = [0] * (len(matrix[0]) + 1)
        self.mat_prefix.append(row)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        all_reg = self.mat_prefix[row2][col2]
        add_reg = self.mat_prefix[row1 - 1][col1 - 1]
        hor_reg = self.mat_prefix[row1 - 1][col2]
        ver_reg = self.mat_prefix[row2][col1 - 1]
        ans = all_reg + add_reg - hor_reg - ver_reg
        return ans
