class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0 for _ in range(len(rooms))]
        queue = deque([0])
        visited[0] = 1
        vr = 1

        while queue:
            room = queue.popleft()
            for rm in rooms[room]:
                if not visited[rm]:
                    queue.append(rm)
                    visited[rm] = 1
                    vr += 1
        
        return vr == len(rooms)
