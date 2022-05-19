class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        c = 0
        for idx, el in enumerate(s):
            sub = s[idx: idx+k]
            if len(sub) == k and int(sub) != 0 and num % int(sub) == 0:
                c += 1
                
        return c
                