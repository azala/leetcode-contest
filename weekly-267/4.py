# pyrival DSU implementation 
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ret = []
        dsu = DSU(n) # use disjoin subset union to keep track of indirect friendships
        for a, b in requests:
            da, db = dsu.find(a), dsu.find(b)
            if da == db:
                ret.append(True) # already friends
            else:
                succ = True
                for c, d in restrictions:
                    # we can't join a and b if:
                    # a is in c's group, and b is in d's, or
                    # a is in d's group, and b is in c's
                    dc, dd = dsu.find(c), dsu.find(d)
                    if (dc == da and dd == db) or (dc == db and dd == da):
                        succ = False
                        break
                if succ:
                    dsu.union(a, b)
                ret.append(succ)
        return ret