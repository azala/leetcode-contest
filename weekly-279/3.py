class Bitset:

    def __init__(self, size: int):
        self.b = False
        self.s = [False] * size
        self.ct = 0

    def valat(self, idx:int) -> bool:
        x = self.s[idx]
        if self.b:
            x = not x
        return x
        
    def fix(self, idx: int) -> None:
        if not self.valat(idx):
            if self.s[idx]:
                self.ct -= 1
            else:
                self.ct += 1
            self.s[idx] = not self.s[idx]

    def unfix(self, idx: int) -> None:
        if self.valat(idx):
            if self.s[idx]:
                self.ct -= 1
            else:
                self.ct += 1
            self.s[idx] = not self.s[idx]

    def flip(self) -> None:
        self.b = not self.b

    def all(self) -> bool:
        if self.b:
            return self.ct == 0
        else:
            return self.ct == len(self.s)

    def one(self) -> bool:
        if self.b:
            return self.ct != len(self.s)
        else:
            return self.ct != 0

    def count(self) -> int:
        x = self.ct
        if self.b:
            x = len(self.s) - x
        return x

    def toString(self) -> str:
        ret = []
        for i in range(len(self.s)):
            if self.valat(i):
                ret.append('1')
            else:
                ret.append('0')
        return ''.join(ret)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
