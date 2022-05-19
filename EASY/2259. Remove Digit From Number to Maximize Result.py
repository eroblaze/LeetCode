class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        d_map = []
        
        for idx, el in enumerate (number):
            if el == digit:
                d_map.append(number [:idx]+number [idx+1:])
                
        n = map(int, d_map)
        return str(max(n))