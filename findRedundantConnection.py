class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        size = [1 for _ in range(len(edges))]
        ans = [1, 1]
        def find(val):
            if parent[val] == val:
                return val
            parent[val] = find(parent[val])
            return parent[val]
        
        def union(x, y):
            nonlocal ans
            parentX = find(x - 1)
            parentY = find(y - 1)

            if parentX != parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]
            else:
                ans = [x, y]
            

        for a, b in edges:
            union(a, b)
        return ans
