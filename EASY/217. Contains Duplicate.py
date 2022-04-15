from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return  c.most_common()[0][1] > 1