class Solution:
    def helper_merge(self,array, index, number,position_string):
        if (position_string == "AFTER"):
            array.insert(index+1, number)
            array.pop()

        elif (position_string == "BEFORE"):
            # position_string is "BEFORE"	
            array.insert(index, number)
            array.pop()
            
    def sort_array(self, array: list[int]):
        array.sort()

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length = m+n
        count = 0
        if (bool(nums2)):
            while count < length:
                if (bool(nums2)):
                    if (nums1[count] == 0):
                        self.helper_merge(nums1, count, nums2[0], "BEFORE");
                        first = nums2[0]
                        nums2.remove(first) 
                        count+=1

                    elif (nums2[0] >= nums1[count] and nums2[0] <= nums1[count+1]):
                        # insert nums2[count] after count
                        self.helper_merge(nums1, count, nums2[0], "AFTER");
                        first = nums2[0]
                        nums2.remove(first) 
                        count+=2

                    elif (nums2[0] >= nums1[count]):
                        # The reason it will enter here is that the next element in nums1 is lesser than the current element in nums2
                        count+=1	

                    elif (nums2[0] < nums1[count]):
                        self.helper_merge(nums1, count, nums2[0], "BEFORE");
                        first = nums2[0]
                        nums2.remove(first) # To remove the first el in nums2
                        count+=2

                    else:
                        count+=1
                else:
                    count+=1
                
        self.sort_array(nums1)
