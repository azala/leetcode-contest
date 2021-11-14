# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def process(node, ln): # process the next (ln) nodes, reversing if length even
            # gather values in array
            cur = node
            values = []
            for i in range(ln):
                if cur is None:
                    break
                values.append(cur.val)
                cur = cur.next
                
            # reverse
            if len(values) % 2 == 0:
                values = values[::-1]
                
            # place values in array
            cur = node
            for i in range(ln):
                if cur is None:
                    break
                cur.val = values[i]
                cur = cur.next
        cur = head
        ct = 1 # number of nodes to process in this chunk
        while 1:
            process(cur, ct)
            for i in range(ct):
                cur = cur.next
                if not cur:
                    return head
            ct += 1