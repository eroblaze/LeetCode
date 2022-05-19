class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        lower = num1 if len(num1) < len(num2) else num2
        higher = num2 if len(num2) > len(num1) else num1
        
        rem = 0
        res = ""
        for i in range(len(lower)):
            # add the last ints
            n = int(lower[-1]) + int(higher[-1]) + rem
            print("n", n)
            
            if len(str(n)) > 1:
                # there is a remainder
                # take the last digit and add the rem count
                res = str(n)[-1] + res
                rem = int(str(n)[:-1])
                print("rem",rem)
            else:
                res = str(n) + res
                rem = 0
                print("res", res)
                
            higher = higher[:-1]
            lower = lower[:-1]
        print(higher, rem, res)
            
        if higher:
            res = str(int(higher) + rem) + res
        elif rem:
            res = str(rem) + res
            
        return res