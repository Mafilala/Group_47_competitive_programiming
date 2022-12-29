class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        min_ = float('inf')
        for idx, coor in enumerate(points):
            if x == coor[0] or y == coor[1]:
                md = abs(x - coor[0]) + abs(y - coor[1])
                if md < min_:
                    min_ = md
                    ans = idx
        return ans
