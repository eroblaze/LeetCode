class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        c = 0
        init_left = nums[:1]
        init_right = nums[1:]
        
        l_sum = sum(init_left)
        r_sum = sum(init_right)
        
        # 2 length
        if len(nums) == 2: return 1 if l_sum >= r_sum else 0
        if l_sum >= r_sum: c += 1 # for the first index
            
        for i in range(1, len(nums)-1):
            l_sum += nums[i]
            r_sum -= nums[i]
            
            if l_sum >= r_sum: c += 1
        
        return c
