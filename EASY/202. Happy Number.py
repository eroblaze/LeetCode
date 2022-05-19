class Solution:
    def isHappy(self, n: int) -> bool:
        # if the sum of the square adds up to the initial input, return false
        
        num = str(n)
        c = 0
        
        while c < 1000:
            _sum = sum([int(i) ** 2 for i in num])
            if _sum == 1: return True
            if _sum == n: return False
            num = str(_sum)
            c += 1
        
        return False