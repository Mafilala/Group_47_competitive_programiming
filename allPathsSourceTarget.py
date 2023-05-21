class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        N = len(graph)
        def dfs(node, path):
            if path and path[-1] == N - 1:
                ans.append(path.copy())
            for adj in graph[node]:
                path.append(adj)
                dfs(adj, path)
                path.pop()
        dfs(0, [0])
        return ans
