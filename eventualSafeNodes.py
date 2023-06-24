class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        def dfs(node, color):
            color[node] = 1
            for child in graph[node]:
                if color[child] == 2:
                    continue
                if color[child] == 3 or color[child] == 1:
                    return False
                if not dfs(child, color):
                    color[child] = 3
                    return False
            color[node] = 2
            return True
        color = [0] * N
        for i in range(N):
            if color[i] == 0:
                dfs(i, color)
        print(color)
        return [i for i in range(N) if color[i] == 2]
