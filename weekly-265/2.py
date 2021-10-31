# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ret = []
        cur = head
        while cur:
            ret.append(cur.val)
            cur = cur.next
            
        first = None
        last = None
        
        mn = float('inf')
        mx = -1
            
        for i in range(1, len(ret)-1):
            if (ret[i-1] < ret[i] and ret[i+1] < ret[i]) or (ret[i-1] > ret[i] and ret[i+1] > ret[i]):
                if last is not None:
                    mn = min(mn, i - last)
                last = i
                if first is None:
                    first = i
                else:
                    mx = i - first
        if mx == -1:
            return [-1, -1]
        else:
            return [mn, mx]