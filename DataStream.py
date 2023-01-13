class DataStream:

    def __init__(self, value: int, k: int):
        self.substream = deque()
        self.value = value
        self.k = k
        self.vp = dict()

    def consec(self, num: int) -> bool:
        self.substream.append(num)
        self.vp[num] = self.vp.get(num, 0) + 1
        if len(self.substream) > self.k:
            popped_val = self.substream.popleft()
            self.vp[popped_val] -= 1
            if self.vp[popped_val] == 0:
                self.vp.pop(popped_val)
        if len(self.vp) > 1 or len(self.substream) < self.k or self.vp.get(self.value, 'No') == 'No':
            return False
        return True
