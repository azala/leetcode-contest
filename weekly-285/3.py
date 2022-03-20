class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        aa_left = [0] * len(aliceArrows)
        aa_left[0] = 0
        for i in range(1, len(aliceArrows)):
            aa_left[i] = aa_left[i-1] + aliceArrows[i] + 1
        aap1 = [x+1 for x in aliceArrows]
        aap1[0] = 0
        
        @cache
        def f(idx, arrows_left):
            if idx == 0:
                return (0, [0])
            if aa_left[idx] <= arrows_left:
                return ((idx) * (idx+1) // 2, aap1[:idx+1])
            val, ret = f(idx-1, arrows_left)
            ret = ret[:] + [0]
            if arrows_left >= aap1[idx]:
                nv, nr = f(idx-1, arrows_left-aap1[idx])
                nv += idx
                if nv > val:
                    val, ret = nv, nr
                    ret = ret[:] + [aap1[idx]]
            return val, ret
        
        a, b = f(11, numArrows)
        b[0] = numArrows - sum(b)
        return b