class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) ->     float:
        new_arr = []
        highest = nums1 if len(nums1) >= len(nums2) else nums2
        lowest = nums1 if len(nums1) < len(nums2) else nums2
        
        while highest and lowest:
            if highest[0] < lowest[0]: new_arr.append(highest.pop(0))
            else: new_arr.append(lowest.pop(0))
        
        rem = highest if highest else lowest
        if rem:
            if new_arr:
                if new_arr[-1] <= rem[0]: new_arr.extend(rem)
                else: new_arr = [*rem, *new_arr]   
            else: new_arr = [*rem]
        
        # if the length is odd
        if len(new_arr) % 2 == 1:
            median = new_arr[(len(new_arr)-1) // 2]
            return median
        else:
            median = (len(new_arr)-1) // 2
            least = new_arr[median]
            great = new_arr[median+1]
            return (least + great) / 2
            
