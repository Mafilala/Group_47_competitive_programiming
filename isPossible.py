class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        for n in nums:
            while heap and heap[0][0] + 1 < n:
                v, l = heappop(heap)
                if l < 3:
                    return False

            if not heap:
                li = [n, 1]
                heappush(heap, li)
            
            else:
                if heap[0][0] == n:
                    heappush(heap, [n, 1])
                else:
                    v, l = heappop(heap)
                    heappush(heap, [n, l + 1])
        while heap:
            _, l = heappop(heap)
            if l < 3:
                return False
        return True
