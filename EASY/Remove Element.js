/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    const ORIGINALLENGTH = nums.length;
    let occurrence = 0;
    let position = 0;
    let tempNum = null;
    
    
    for (let i = 0; i < nums.length;) {
        if (nums[i] !== val) {
            tempNum = nums[i];
            nums.splice(position,0, tempNum);
            position++;
            i += 2;
        } else {
         i++;
        }
    }
    
    for (let i = position; i < nums.length; i++) {
        nums[i] = null;
    }
    
    nums.splice(ORIGINALLENGTH);
    
    return position;    
};