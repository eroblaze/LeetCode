/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let firstNum;
    let resArr = [];
    
    for (let i = 0; i < nums.length; i++) {
        firstNum = nums[i];
        for ( let j = i + 1; j < nums.length; j++) {
            if (firstNum + nums[j] === target) {
                resArr.push(i, j);
            }
        }
    }
    
    return resArr;
    
};