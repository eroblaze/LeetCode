class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # There will always be 0,0 ways
        c = 0
        t = total
        h = max(cost1, cost2)
        l = min(cost1, cost2)
        m = h
        if total < l: return 1
        
        # 0 h
        c += t // l
        c += 1
        
        while t >= m:
            r = t - m
            if r >= l: 
                c += r // l
            c += 1
            m += h
        
        return c