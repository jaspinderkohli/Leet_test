class RecentCounter:

    def __init__(self):
        self.requests = []
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        start_time = t -3000
        while self.requests[0] < start_time:
            self.requests.pop(0)
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
