class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = dict(Counter(s1))
        win_size = len(s1)
        for r in range(len(s2) - win_size + 1):
            check = dict(Counter(s2[r: r + win_size]))
            if check == target:
                return True
        return False
