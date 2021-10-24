class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        MAXN = int(1e6)
        
        # return frequency of each digit in x
        def cts(x):
            d = {}
            for c in str(x):
                ic = int(c)
                if ic not in d:
                    d[ic] = 0
                d[ic] += 1
            return d
            
        for i in range(n+1, MAXN+1):
            d = cts(i)
            is_beautiful = True
            for k in d:
                if d[k] != k:
                    is_beautiful = False
                    break
            if is_beautiful:
                return i
            
        # max n is 1000000, so if it hasn't been found yet, this is the answer
        return 1224444