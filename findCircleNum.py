class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        visited = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(i)
                    graph[j].append(i)
        
        def dfs(city):
            visited[city] = 1
            for neighbour in graph[city]:
                if not visited[neighbour]:
                    dfs(neighbour)

        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
        return res
