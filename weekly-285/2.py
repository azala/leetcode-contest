class Solution:
    def countCollisions(self, directions: str) -> int:
        ns, nl, nr = 0, 0, 0
        for i in range(len(directions)):
            if directions[i] == 'L':
                nl += 1
            else:
                break
        for i in range(len(directions)-1, -1, -1):
            if directions[i] == 'R':
                nr += 1
            else:
                break
        for d in directions:
            if d == 'S':
                ns += 1
        return len(directions) - ns - nl - nr