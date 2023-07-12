class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        size = [1 for _ in range(n)]

        def find(val):
            if root[val] == val:
                return val
            root[val] = find(root[val])
            return root[val]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                if size[px] > size[py]:
                    root[py] = px
                    size[px] += size[py]
                else:
                    root[px] = py
                    size[py] += size[px]
        
        for a, b in edges:
            union(a, b)
        ans = find(source) == find(destination)
        return ans
