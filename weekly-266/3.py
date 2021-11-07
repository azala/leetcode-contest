class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # if we can assign x products per store, is it possible to fit all quantities in n stores?
        def can(x):
            ret = 0
            for q in quantities:
                # we need ceiling(q/x) stores
                ret += q//x + int(q%x > 0)
                if ret > n:
                    return False
            return True
        
        # binary search on possible values
        l = 1
        r = max(quantities) # you never need more than the largest quantity because at that point you can throw everything in 1 store per product type
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi+1
        return l
            