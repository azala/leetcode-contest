class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # build the graph
        g = [[] for _ in range(len(parents))]
        for i, p in enumerate(parents):
            if p != -1:
                g[p].append(i)
        
        n = len(parents)
        best = -1 # highest product
        ct = 0 # number of nodes with that product
        
        def dfs(x):
            nonlocal best, ct
            # get number of nodes in the subtrees of children
            l = [dfs(ch) for ch in g[x]]
            # there are three possible remaining trees:
            # let L = number in left child
            # let R = number in right child
            # product = max(1, (n - L - R - 1)) * max(1, L) * max(1, R)
            count_nodes = sum(l) + 1
            ret = max(1, (n - count_nodes))
            for x in l:
                ret *= x
            if ret > best:
                best = ret
                ct = 1
            elif ret == best:
                ct += 1
            # return the number of nodes in the subtree rooted at x
            return count_nodes
        dfs(0)
        return ct