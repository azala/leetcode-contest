class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d = {}
        for i, e in enumerate(arr):
            if e not in self.d:
                self.d[e] = []
            self.d[e].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.d:
            return 0
        l = bisect.bisect_left(self.d[value], left)
        r = bisect.bisect_left(self.d[value], right+1)
        return r - l


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)