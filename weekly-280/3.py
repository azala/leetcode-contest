class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        tot = sum(beans)
        mn = tot
        for i in range(len(beans)):
            mn = min(mn, tot - (beans[i] * (len(beans)-i)))
        return mn