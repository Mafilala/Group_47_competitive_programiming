class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        parent = [i for i in range(n)]
        size = [ 1 for _ in range(n)]
        
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parX = find(x)
            parY = find(y)
            
            if parX == parY:
                return 
            
            if size[parX] > size[parY]:
                parent[parY] = parent[parX]
                size[parX] += size[parY]
                
            else:
                parent[parX] = parent[parY]
                size[parY] += size[parX]
                
        for a, b in pairs:
            union(a, b)
            
        connected = defaultdict(list)
        
        for i in range(n):
            connected[find(parent[i])].append(i)
         
        result = [ch for ch in s]
        
        for cons in connected.values():
            chars = []
            
            for ind in cons:
                chars.append(s[ind])
            chars.sort()
            
            count = 0
            for ind in cons:
                result[ind] =chars[count]
                count += 1
                
        return "".join(result)
