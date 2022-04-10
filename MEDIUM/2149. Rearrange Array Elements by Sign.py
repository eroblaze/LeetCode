class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        The index of an element in the returned array must can be less than its position in the original array by 1 but not more than
        """
        pos = [i for i in nums if i >= 0]
        neg = [i for i in nums if i < 0]
        r = []
        for i in range(len(pos)):
            r.append(pos[i])
            r.append(neg[i])
        return r