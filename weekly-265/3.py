class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        dp = [None] * 1001
        dp[start] = 0
        
        q = [start]
        qp = 0
        
        while qp < len(q):
            cur = q[qp]
            for n in nums:
                for v in [cur+n, cur-n, cur^n]:
                    if v == goal:
                        return dp[cur] + 1
                    elif 0 <= v <= 1000 and dp[v] is None:
                        dp[v] = dp[cur] + 1
                        q.append(v)
            qp += 1
                        
        return -1