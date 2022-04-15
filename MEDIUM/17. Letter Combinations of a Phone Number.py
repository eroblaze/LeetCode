from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return []
        
        d_to_l = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        if len(digits) == 1:
            return list(d_to_l[digits])
        
        conv = [d_to_l[i] for i in digits]
        
        p = list(product(*conv))
        r = map(lambda x: "".join(x), p)
        return r
        