class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        cnt = 0
        for i in range(r - 2):
            for j in range(c - 2):
                r1 = grid[i][j: j + 3]
                r2 = grid[i + 1][j: j + 3]
                r3 = grid[i + 2][j: j + 3]
                c1 = r1[0] + r2[0] + r3[0]
                c2 = r1[1] + r2[1] + r3[1]
                c3 = r1[2] + r2[2] + r3[2]
                d1 = r1[0] + r2[1] + r3[2]
                d2 = r1[2] + r2[1] + r3[0]
                distinict = len([*r1, *r2, *r3]) == len(set([*r1, *r2, *r3]))
                one_nine = set([*r1, *r2, *r3]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}
                if sum(r1) == sum(r2) == sum(r3) == c1 == c2 == c3 == d1 == d2 and distinict and one_nine:
                    cnt += 1
        return cnt
