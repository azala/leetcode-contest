class Solution:
    def subStrHash(self, s: str, p: int, m: int, k: int, v: int) -> str:
        cur = 0
        best = 1e9
        q = pow(p, k, m)
        for i in range(len(s)-1, -1, -1):
            cur = (p * cur + ord(s[i]) - ord('a') + 1) % m
            if i <= len(s) - k - 1:
                cur -= q * (ord(s[i+k]) - ord('a') + 1)
                cur = ((cur % m) + m) % m
            # print(i, cur)
            if i <= len(s) - k:
                if cur == v:
                    best = i
        return s[best:best+k]