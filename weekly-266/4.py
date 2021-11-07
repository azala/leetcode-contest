class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        g = [{} for _ in range(n)]
        for x, y, t in edges:
            g[x][y] = t
            g[y][x] = t

        cv = values[0] # current value of path in DFS
        mx = values[0] # max value of a valid path
        path = {0: 1} # number of times we've visited a node in the current path
        def dfs(cur, tl):
            nonlocal mx, cv
            
            # if we're at 0, we currently have a valid path
            if cur == 0:
                mx = max(mx, cv)
                
            # try all adjacent nodes
            for nx in g[cur]:
                cost = g[cur][nx]
                if tl >= cost:
                    exists = nx in path
                    if exists:
                        path[nx] += 1
                    else:
                        path[nx] = 1
                        # we only increment the current value if we've never seen the node on this path
                        cv += values[nx]

                    dfs(nx, tl - cost)

                    # backtrack DFS
                    if exists:
                        path[nx] -= 1
                    else:
                        del path[nx]
                        cv -= values[nx]
        dfs(0, maxTime)
        return mx
                