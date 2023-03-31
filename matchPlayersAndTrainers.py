class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matches = 0
        i, j = 0, 0
        limit = min(len(players), len(trainers))
        players = players[:limit]
        trainers = trainers[len(trainers) - limit:]
        matches = 0
        while i < limit and j < limit:
            p = players[i]
            t = trainers[j]
            if p <= t:
                matches += 1
                i += 1
                j += 1
            else:
                j += 1

        return matches
