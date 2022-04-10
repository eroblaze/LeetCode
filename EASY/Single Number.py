from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        print(list(c))
        return c.most_common()[-1][0]
