class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = defaultdict(tuple)
        size = defaultdict(lambda: 1)

        def find(val):
            if parent[val] == ():
                return val
            parent[val] = find(parent[val])
            return parent[val]
        
        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]

        i = 1
        for a, b in stones:
            for c, d in stones[i:]:
                if a == c or b == d:
                    union((a, b), (c, d))
            i += 1
        cnt = 0
        for a, b in stones:
            if parent[(a, b)] == ():
                cnt += 1
        return len(stones) - cnt
