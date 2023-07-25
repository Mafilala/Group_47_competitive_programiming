class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n + 1)]
        size = [1 for _ in range(n + 1)]
        short = [float('inf') for _ in range(n + 1)]

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y, d):
            parentX = find(x)
            parentY = find(y)

            if parentX == parentY:
                short[parentX] = min(short[parentX], d)
                return
            if size[parentX] > size[parentY]:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
                short[parentX] = min(short[parentX], d)
            else:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
                short[parentY] = min(short[parentY], d)

        for a, b, d in roads:
            union(a, b, d)

        connected = defaultdict(set)
        for i in range(1, n + 1):
            connected[find(parent[i])].add(i)
        for con in connected.values():
            ans = float('inf')
            if 1 in con and n in con:
                while con:
                    ans = min(ans, short[con.pop()])
                return ans
        
