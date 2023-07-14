class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]

        def find(val):
            if val == parent[val]:
                return val
            parent[val] = find(parent[val])
            return parent[val]
        
        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                if parentX < parentY:
                    parent[parentY] = parentX
                else:
                    parent[parentX] = parentY
        
        for i in range(len(s1)):
            a = ord(s1[i]) - ord('a')
            b = ord(s2[i]) - ord('a')
            union(a, b)
        ans = ''
        for letter in baseStr:
            ans += chr(find(ord(letter) - ord('a')) + ord('a'))
        return ans
