class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = []
        loser = []
        for match in matches:
            winner.append(match[0])
            loser.append(match[1])
        answer = []
        a1 = list(set(winner) - set(loser))
        a2 = []
        cnt = Counter(loser)
        for k, v in cnt.items():
            if v == 1:
                a2.append(k)
        answer.append(sorted(a1))
        answer.append(sorted(a2))
        return answer
