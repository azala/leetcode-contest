class Solution:
    def minimumTime(self, s: str) -> int:
        # idea: for every possible left cutoff (from 0 to len(s) cars) figure out the most advantageous right cutoff
        # memoizing "most advantageous right cutoff" in best_to_right below cuts the overall runtime to O(len(s))
        
        best_to_right = [0] * (len(s)+1) 
        cost_from_right = 0
        for i in range(len(s)-1, -1, -1):
            cost_from_right += 1 # cutting an extra car costs 1
            if s[i] == '1':
                cost_from_right -= 2 # but if it's illegal, subtract 2 from the cost of the move
            best_to_right[i] = min(cost_from_right, best_to_right[i+1]) # track the running "most advantageous right side cut off so far"
        
        cur_cost = 0
        for c in s:
            if c == '1':
                cur_cost += 2
        ret = cur_cost + best_to_right[0] # best cost if you take nothing from left
        for i in range(len(s)):
            cur_cost += 1
            if s[i] == '1':
                cur_cost -= 2
            ret = min(ret, cur_cost + best_to_right[i+1]) # best cost if you take (i+1) from left
        return ret