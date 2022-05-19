from functools import reduce

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        higher = num1 if len(num1) > len(num2) else num2 
        lower = num2 if len(num2) < len(num1) else num1
            
        res = ""
        c = 0
        keep = []        

        for i in range(len(lower)):
            for j in range(len(higher)-1, -1, -1):
                p = (int(lower[-1]) * int(higher [j]) ) + c
                
                if len(str(p)) > 1:
                    if j == 0:
                        res = str(p) + res
                        c = 0
                        keep.append(str(res) + ("0" * i))
                        res = ""
                    else:
                        res = str(p)[-1] + res
                        c = int(str(p)[:-1])
                
                else:
                    if j == 0:
                        res = str(p) + res
                        c = 0
                        keep.append(str(res) + ("0" * i))
                        res = ""
                    else:
                        res = str(p) + res
                        c = 0

            lower = lower [:-1]
            
        sum = reduce (lambda a, e: int(a) + int(e), keep)
  
        return str(sum) if any(int(i) > 0 for i in str(sum)) else "0"