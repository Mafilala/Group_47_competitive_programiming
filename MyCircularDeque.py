class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.queue = deque()
        self.s = 0
        self.e = 0

    def insertFront(self, value: int) -> bool:
        if self.e - self.s >= self.size:
            return False
        self.queue.append(value)
        self.e += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.e - self.s >= self.size:
            return False
        self.queue.appendleft(value)
        self.s -= 1
        return True

    def deleteFront(self) -> bool:
        if self.e == self.s:
            return False
        self.queue.pop()
        self.e -= 1
        return True

    def deleteLast(self) -> bool:
        if self.e == self.s:
            return False
        self.queue.popleft()
        self.s += 1
        return True

    def getFront(self) -> int:
        return self.queue[-1] if self.e > self.s else -1

    def getRear(self) -> int:
        return self.queue[0] if self.e > self.s else -1

    def isEmpty(self) -> bool:
        return self.s == self.e

    def isFull(self) -> bool:
        return self.e - self.s >= self.size
