class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ret = 0
        while 1:
            if num1 == 0 or num2 == 0:
                return ret
            if num1 >= num2:
                num1 -= num2
            elif num2 >= num1:
                num2 -= num1
            ret += 1