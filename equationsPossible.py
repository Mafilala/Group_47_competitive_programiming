class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        print(parent)
        size = [1 for _ in range(26)]

        def find(val):
            if val == parent[val]:
                return val
            parent[val] = find(parent[val])
            return parent[val]
        
        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if size[parentX] > size[parentY]:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
            else:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
        
        checker = []
        for eq in equations:
            a = ord(eq[0]) - ord('a')
            b = ord(eq[3]) - ord('a')
            print(a, b)
            if eq[1] == '!':
                checker.append(eq)
            else:
                union(a, b)
        
        for ch in checker:
            a = ord(ch[0]) - ord('a')
            b = ord(ch[3]) - ord('a')
            if find(a) == find(b):
                return False
        return True
