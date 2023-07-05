class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        incoming = defaultdict(int)
        graph = defaultdict(list)
        for p1, p2 in adjacentPairs:
            incoming[p1] += 1
            incoming[p2] += 1
            graph[p1].append(p2)
            graph[p2].append(p1)

        queue = deque()
        visited = set()
        ans = []
        for k in incoming.keys():
            if incoming[k] == 1:
                queue.append(k)
                visited.add(k)
                break
        while queue:
            popped = queue.popleft()
            ans.append(popped)
            for child in graph[popped]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        return ans
