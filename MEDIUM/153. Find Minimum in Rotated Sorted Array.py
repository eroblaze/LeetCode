class Solution:
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            radix = nums[0] # forgotten the real name
            less = []
            great = []
            for i in range(1,len(nums)):
                if nums[i] <= radix:
                    less.append(nums[i])
                else:
                    great.append(nums[i])
                    
            less = self.quicksort(less)
            great = self.quicksort(great)
            
            return less + [radix] + great
        
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums = self.quicksort(nums)
        return nums[0]