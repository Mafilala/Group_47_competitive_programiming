class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key=lambda li: (-abs(li[0] - li[1])))
        n = len(costs) // 2
        a = 0
        b = 0
        total = 0
        for ca, cb in costs:
            if ca < cb:
                if a < n:
                    a += 1
                    total += ca
                else:
                    b += 1
                    total += cb
            else:
                if b < n:
                    b += 1
                    total += cb
                else:
                    a += 1
                    total += ca
        return total
