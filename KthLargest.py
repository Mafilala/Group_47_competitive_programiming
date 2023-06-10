class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.kstream = nums[:k]
        heapify(self.kstream)

    def add(self, val: int) -> int:
        if not self.kstream or val > self.kstream[0] or len(self.kstream) < self.k:
            heappush(self.kstream, val)
            if len(self.kstream) > self.k:
                heappop(self.kstream)
        return self.kstream[0]
            
