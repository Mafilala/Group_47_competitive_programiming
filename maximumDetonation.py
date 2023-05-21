class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        N = len(bombs)
        for i in range(N):
            par = bombs[i]
            x1, y1, r1 = par[0], par[1], par[2]
            for j in range(i + 1, N):
                par1 = bombs[j]
                x2, y2, r2 = par1[0], par1[1], par1[2]
                x = abs(x2 - x1)
                y = abs(y2 - y1)
                dist = sqrt(x ** 2 + y ** 2)
                if r1 >= dist:
                    graph[i].append(j)
                if r2 >= dist:
                    graph[j].append(i)

        def dfs(node, visited):
            visited[node] = 1
            for nd in graph[node]:
                if not visited[nd]:
                    dfs(nd, visited)
        
        max_ = 1
        for i in range(N):
            visited = [0 for _ in range(N)]
            dfs(i, visited)
            count = visited.count(1)
            if count == N:
                max_ = N
                break
            max_ = max(max_, count)
        return max_
