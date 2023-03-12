class RecentCounter:

    def __init__(self):
        self.r_request = deque()
        self.n_request = 0

    def ping(self, t: int) -> int:
        self.r_request.append(t)
        while self.r_request and t - self.r_request[0] > 3000:
            self.r_request.popleft()
        return len(self.r_request)
