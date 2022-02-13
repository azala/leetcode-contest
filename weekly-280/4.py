class Solution:
    def maximumANDSum(self, A, ns):
        @lru_cache(None)
        def dp(i, profile):
            if i == len(A): return 0
            ret = 0
            for j in range(ns):
                if profile[j] < 2:
                    new_profile = list(profile)
                    new_profile[j] += 1
                    ret = max(ret, (A[i] & (j+1)) + dp(i+1, tuple(new_profile)))
            return ret
        return dp(0, tuple(list([0] * ns)))