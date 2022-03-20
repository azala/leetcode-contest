class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        x = []
        for n in nums:
            if not len(x) or n != x[-1]:
                x.append(n)
        ret = 0
        for i in range(1, len(x)-1):
            l, r = x[i-1], x[i+1]
            if l < x[i] and r < x[i]:
                ret += 1
            elif l > x[i] and r > x[i]:
                ret += 1
        return ret