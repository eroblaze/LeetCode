from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = [list (i) for i in list(permutations (nums))]
        return p