class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        o, e = [], []
        for i in range(len(nums)):
            if i % 2:
                o.append(nums[i])
            else:
                e.append(nums[i])
        o.sort(reverse=True)
        e.sort()
        ret = []
        a, b = 0, 0
        for i in range(len(nums)):
            if i % 2:
                ret.append(o[i//2])
            else:
                ret.append(e[i//2])
        return ret