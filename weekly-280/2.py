class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = {}
        e = {}
        for i in range(len(nums)):
            x = d if (i % 2) else e
            if i % 2:
                cd += 1
            else:
                ce += 1
            x[nums[i]] = x.get(nums[i], 0) + 1
            
        d[''] = 0
        e[''] = 0
        
        dd = sorted(d.items(), key=lambda x: -x[1])
        ee = sorted(e.items(), key=lambda x: -x[1])
        
        if dd[0][0] == ee[0][0]:
            f = max(dd[0][1] + ee[1][1], dd[1][1] + ee[0][1])    
        else:
            f = dd[0][1] + ee[0][1]
        
        return len(nums) - f