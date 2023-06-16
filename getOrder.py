class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        idx = 0
        order = [] #based on enque time
        idx = 0
        ans = []
        for et, pt in tasks:
            heappush(order, (et, pt, idx))
            idx += 1
        heap = [] #based on process time
        et, pt, idx = heappop(order)
        heappush(heap,(pt, idx, et))
        time = heap[0][2]
        while heap:
            pt, idx, et = heappop(heap)
            time += pt
            ans.append(idx)
            while order and order[0][0] <= time:
                enqt, prct, index = heappop(order)
                heappush(heap, (prct, index, enqt))
            if not heap and order:
                time = order[0][0]
            while order and order[0][0] <= time:
                enqt, prct, index = heappop(order)
                heappush(heap,( prct, index, enqt))
                
        return ans
