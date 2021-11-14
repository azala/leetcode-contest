class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ret = 0
        while 1: # infinite loop
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1 # simulate i-th person buying a ticket
                    ret += 1
                if tickets[k] == 0:
                    return ret # we have just simulated the k-th person buying their last ticket