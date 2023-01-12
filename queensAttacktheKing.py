class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [[0, -1],[0, 1], [-1, 0], [1, 0],[1, 1], [1, -1], [-1, 1], [-1, -1]]
        possible_attacks = []
        for d in directions:
            i, j = king
            while 0 <= i <= 7 and 0 <= j <= 7:
                suspect = [i, j]
                if suspect in queens:
                    possible_attacks.append(suspect)
                    break
                else:
                    i += d[0]
                    j += d[1]
        return possible_attacks
