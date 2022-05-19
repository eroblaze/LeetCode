class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) < k: return s
        t = s
        
        a = [""]
        c = 0
        while len(t) > k:
            for i in t:
                if c >= k:
                    a.append(f"{i}")
                    c = 0
                else: a[-1]+=i
                c+=1
                

            g = []
            for i in a:
                p = list(i)
                o = [int(z) for z in p]
                g.append(sum(o))
                
                
            t = "".join([str(l) for l in g])

            a = [""]
            c = 0
        
                                
        return t
                                             
        