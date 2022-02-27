class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ret = 0
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            d[c] = d.get(c, 0) - 1
        for k in d:
            ret += abs(d[k])
        return ret