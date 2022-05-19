class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        new_arr = [abs(i) for i in nums]
        m = min(new_arr)
        return m if m in nums else -m
