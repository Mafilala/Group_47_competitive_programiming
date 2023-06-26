class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i: [] for i in range(n)}
        incoming = [0] * n
        ans = [[] for _ in range(n)]
        for a, b in edges:
            graph[b].append(a)
        def dfs(kid, ans, visited):
            for anc in graph[kid]:
                if anc in visited:
                    continue
                visited.add(anc)
                ans.append(anc)
                dfs(anc, ans, visited)
        
        for i in range(n):
            dfs(i,ans[i], set())
        return [sorted(ans[i]) for i in range(n)]
