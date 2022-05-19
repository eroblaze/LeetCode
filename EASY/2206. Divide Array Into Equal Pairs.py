from collections import Counter 

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = dict(Counter (nums))
        return all(i % 2 == 0 for i in c.values())