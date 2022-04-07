/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const originalLength = nums.length;
    let repeated = null;
    let unique = 0;
    
    for(let i = 0; i < nums.length; ) {
        if (nums[i] === repeated) {
            i++;
        }
        else if (nums[i] === nums[i+1]) {
            repeated = nums[i];
            nums.splice(unique,0,repeated);
            i += 3;
            unique++;
        } else {
            nums.splice(unique,0,nums[i]);
            i += 2;
            unique++;
        }
    }
    
    nums.splice(unique)
    
    
    for (let i = unique; i < originalLength; i++) {
        nums.push(null);
    }
    
    return unique;
};