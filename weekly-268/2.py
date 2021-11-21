class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        idx = 0
        cur = []
        sc = 0
        ret = 0
        for i in range(n):
            v = plants[i]
            if sc + v <= capacity:
                cur.append(v)
                sc += v
            else:
                # print(cur)
                ret += 2 * (idx + len(cur))
                idx += len(cur)
                cur = [v]
                sc = v
        # print('ke', cur)
        ret += n
        return ret