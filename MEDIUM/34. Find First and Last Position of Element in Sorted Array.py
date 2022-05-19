class Solution:
    def _left_search(self, nums, middle, target):
        if nums[middle] == target: 
            if middle > 0 and nums[middle-1] == target:
                return "left"
            return "found"
        elif nums[middle] > target: return "left"
        else: return "right"
            
    def _right_search(self, nums, middle, target):
        if nums[middle] == target: 
            if middle < len(nums)-1 and nums[middle+1] == target:
                return "right"
            return "found"
        elif nums[middle] > target: return "left"
        else: return "right"
        
    def binary_search(self, nums, position, target):
        first = 0
        last = len(nums) -1
        while first <= last:
            
            middle = (first + last) // 2
            to_do = position(nums=nums, middle=middle, target=target)
            if to_do == "found": return middle
            elif to_do == "left": last = middle-1
            else: first = middle + 1
                
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary search solution
        return [self.binary_search(nums, self._left_search, target=target), self.binary_search(nums, self._right_search, target=target)]
        
        # brute force solution :
#         if not nums or target not in nums: return [-1, -1]
        
#         t_count = nums.count(target)
#         c_array = []
#         for i in range(t_count):
#             c_array.append((i := nums.index(target)))
#             nums[i] = None
            
#         return [c_array[0], c_array[-1]]

        # O(k) -> where k is the amount of times target occurs in the nums array
    