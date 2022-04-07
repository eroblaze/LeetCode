/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
   return (BigInt(digits.join("")) +1n).toString().split("");
};