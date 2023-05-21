class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [-1 for _ in range(n + 1)]
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, color):
            visited[node] = color
            for neighbour in graph[node]:
                if visited[neighbour] == color:
                    return False
                elif visited[neighbour] == -1:
                    if not dfs(neighbour, color ^ 1):
                        return False
            return True

        for i in range(1, n + 1):
            if visited[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
