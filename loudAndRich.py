class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        parent = [[] for _ in range(len(quiet))]

        queue = deque()
        graph = [[] for _ in range(len(quiet))]
        incoming = [0 for _ in range(len(quiet))]
        for a, b in richer:
            graph[a].append(b)
            incoming[b] += 1
        idx = 0
        for count in incoming:
            if count == 0:
                queue.append(idx)
            idx += 1
        answer = [-1] * len(quiet)
        visited = set()
        while queue:
            popped = queue.popleft()
            if parent[popped] == []:
                answer[popped] = popped
            else:
                ans = popped
                for v in parent[popped]:
                    if quiet[answer[v]] < quiet[ans] and answer[v] != -1:
                        ans = answer[v]
                answer[popped] = ans
            for child in graph[popped]:
                parent[child].append(popped)
                incoming[child] -= 1
                if incoming[child] == 0:
                    queue.append(child)
        return answer
        
