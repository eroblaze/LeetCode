from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        c = list(set (permutations (nums)))
        return c