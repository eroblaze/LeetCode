class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        sl = list(s)
        
        e, o = [], []
        
        for i, el in enumerate(sl):
            if int(el) % 2 == 0:
                e.append((el, i))
            else:
                o.append((el, i))
                
        es = sorted(e, key=lambda x: -int(x[0]))
        
        os = sorted(o, key=lambda y: -int(y[0]))
        
        pl = [-1] * len(s)
     
        for idx, el in enumerate(sl):
            if int(el) % 2 == 0:
                
                if len(es) > 0:
                    
                    if idx != es[0][1] and el != es[0][0]:
                        pl[idx] = es[0][0]
                        pl[es[0][1]] = el if int(pl[es[0][1]]) < 0 else pl[es[0][1]]
                        es.pop(0)
                        
                        print('e pl', pl)
                        print('e', es)
                    
                    else:
                        pl[idx] = el
                        es.pop(0)
                        print ("e pl", pl)
                        print('e', es)
                    
                    
            else:
                if len(os) > 0:
                    
                    if idx != os[0][1] and el != os[0][0]:
                        print('o', os)
                        pl[idx] = os[0][0]
                        pl[os[0][1]] = el if int(pl[os[0][1]]) < 0 else pl[os[0][1]]
                        os.pop(0)
                        print ('o pl', pl)
                        print('o', os)
                        
                    else:
                        pl[idx] = el
                        os.pop(0)
                        print ('o pl', pl)
                        print ('o', os)
                
                    
        r = int("".join(pl))
        
        return r
                    
