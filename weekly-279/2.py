class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        elif num > 0:
            l = [c for c in str(num)]
            l.sort()
            q = None
            for x in l:
                if x != '0':
                    l.remove(x)
                    q = x
                    break
            l = [q] + l
            return int(''.join(l))
        else:
            num = -num
            l = [c for c in str(num)]
            l.sort(reverse=True)
            return -int(''.join(l))
