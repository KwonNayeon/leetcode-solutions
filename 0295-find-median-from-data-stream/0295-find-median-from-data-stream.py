class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if not self.upper or self.upper[0] < num:
            heappush(self.upper, num)
        else:
            heappush(self.lower, -num)

        if len(self.lower) > len(self.upper):
            heappush(self.upper, -heappop(self.lower))
        elif len(self.lower) + 1 < len(self.upper):
            heappush(self.lower, -heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) < len(self.upper):
            return self.upper[0]

        else:
            return (-self.lower[0] + self.upper[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()