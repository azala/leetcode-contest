# very clean sol - credit https://leetcode.com/1015634/
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        @cache
        def ans(x, y, dif):
            print(x, y, dif)
            # Dp s1[x:], s2[y:], s1 has dif more spaces then s2
            if x == n and y == m:
                return dif == 0
            if x == n and dif <= 0:
                return False
            if y == m and dif >= 0:
                return False
            if dif == 0 and x<n and y<m and s1[x].isalpha() and s2[y].isalpha() and s1[x] != s2[y]:
                return False
            if dif >= 0:
                # Advance y
                if s2[y].isalpha() and ans(x, y+1, dif-1):
                    return True
                cur = ''
                for j in range(y, y+3):
                    if j == m or not s2[j].isdigit():
                        break
                    cur += s2[j]
                    if ans(x, j+1, dif-int(cur)):
                        return True
            else:
                # Advance x
                if s1[x].isalpha() and ans(x+1, y, dif+1):
                    return True
                cur = ''
                for j in range(x, x+3):
                    if j == n or not s1[j].isdigit():
                        break
                    cur += s1[j]
                    if ans(j+1, y, dif+int(cur)):
                        return True
            return False
        return ans(0, 0, 0)
                
        
