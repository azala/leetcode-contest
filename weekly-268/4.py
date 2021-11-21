def is_pal(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        ret = []
        for i in range(1, 1000):
            l = (k ** (i-1))
            r = (k ** i)
            for t in range(l, r):
                s = numberToBase(t, k)
                rs = s[::-1]
                x = s + rs[1:]
                x = ''.join([str(u) for u in x])
                q = int(x, k)
                if is_pal(str(q)):
                    ret.append(q)
                    if len(ret) == n:
                        return sum(ret)
            for t in range(l, r):
                s = numberToBase(t, k)
                rs = s[::-1]
                x = s + rs
                x = ''.join([str(u) for u in x])
                q = int(x, k)
                if is_pal(str(q)):
                    ret.append(q)
                    if len(ret) == n:
                        return sum(ret)