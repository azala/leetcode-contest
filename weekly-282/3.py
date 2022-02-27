class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def can(x):
            ret = 0
            for t in time:
                ret += x // t
                if ret >= totalTrips:
                    return True
            return False
        l = 1
        r = int(1e18)
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi+1
        return r