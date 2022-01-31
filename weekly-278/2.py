class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l = 0
        r = sum(nums)
        best = r
        idxs = [0]
        for i in range(len(nums)):
            c = nums[i]
            if c == 0:
                l += 1
            else:
                r -= 1
            if l + r == best:
                idxs.append(i+1)
            elif l + r > best:
                best = l + r
                idxs = [i+1]
        return idxs