class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        mx = 30
        best = [float('inf')] * mx
        dp = [float('inf')] * (numLaps+1)
        dp[0] = 0
        
        n = len(tires)
        acct = [0] * n
        for j in range(len(best)):
            for i in range(n):
                acct[i] *= tires[i][1]
                acct[i] += tires[i][0]
                best[j] = min(best[j], acct[i] + changeTime)
            if j > 0 and best[j] >= best[0] * (j+1):
                mx = j+1
                break
                
        for i in range(1, numLaps+1):
            for j in range(1, mx+1):
                if i-j >= 0:
                    dp[i] = min(dp[i-j] + best[j-1], dp[i])
        return dp[numLaps] - changeTime