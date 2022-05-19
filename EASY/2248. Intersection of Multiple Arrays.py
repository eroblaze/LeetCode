
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1: return sorted(nums[0])
        
        new_set = nums.copy()
        inter = set()
        
        for i in range(len(new_set)):
            if i != len(new_set) -1:
                j = set(new_set[i]) & set(new_set[i+1])
                if not len(inter):
                    for k in j:
                        inter.add(k)
                inter = inter & j
                
        return sorted(list(x)) if (x:= inter) else []