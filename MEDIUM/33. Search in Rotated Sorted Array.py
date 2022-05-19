class Solution:
    def binary_search(self, arr, t):
        first = 0
        last = len(arr)-1
        
        while first <= last and last >= first:
            middle = (first + last) // 2
            if arr[middle] == t: return True
            elif arr[middle] > t: last = middle - 1
            else: first = middle + 1
        
        return False
    
    def search(self, nums: List[int], target: int) -> int:
        cpy = nums[:]
        cpy.sort()
        if self.binary_search(cpy, target): return nums.index(target)
        return -1
        