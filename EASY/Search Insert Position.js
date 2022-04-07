/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    
    // For an array with length of 1;
    if (nums.length === 1 && nums[0] === target) return 0; 
    else if (nums.length === 1 && target > nums[0]) return 1;
    else if (nums.length === 1 && target < nums[0]) return 0;
    
    // length is greater than one
    for (let i = 0; i < nums.length; i++) {
        if (i === 0) {
            if (target < nums[i]) return 0;
        }
        
        if (nums[i] === target) return i;
        else {
            if (target > nums[i] && target < nums[i+1]) {
                return i+1;
            }
            // Have reached the last element in the array and have not found the match in the array, all I need to do now is to return the length of the array
            if (i+1 === nums.length) return nums.length;
        }
    }
    
    
};