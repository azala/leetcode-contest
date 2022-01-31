class DSU:
    def __init__(self, fl):
        n = len(fl)
        self.parent = list(range(n))
        self.size = fl
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        f = {}
        for w in words:
            cur = 0
            for c in w:
                cur += (1 << (ord(c) - 97))
            f[cur] = f.get(cur, 0) + 1
            for i in range(26):
                ncur = cur | (1 << i)
                f[ncur] = f.get(ncur, 0)
        ks = list(f.keys())
        vs = [f[k] for k in ks]
        rm = {}
        for i, k in enumerate(ks):
            rm[k] = i
        dsu = DSU(vs)
        for k in ks:
            if f[k] > 0:
                for i in range(26):
                    ck = k | (1 << i)
                    if k != ck and ck in rm:
                        dsu.union(rm[k], rm[ck])
        return [len(dsu), max(dsu.size)]
        
        