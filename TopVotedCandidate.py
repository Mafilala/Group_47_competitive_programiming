class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.winners = []
        mx = self.persons[0]
        cnt = defaultdict(int)
        for p in self.persons:
            cnt[p] += 1
            if cnt[p] >= cnt[mx]:
                mx = p
            self.winners.append(mx)



        
    def q(self, t: int) -> int:
        l = 0
        r = len(self.times) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if self.times[mid] <= t:
                l = mid
            else:
                r = mid - 1
        return self.winners[l]
