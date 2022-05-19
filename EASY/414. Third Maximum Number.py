class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        check = set(nums)
        if len(check) <= 2: return max(nums)
        for i in range(2):
            check.remove(max(check))
        return max(check)