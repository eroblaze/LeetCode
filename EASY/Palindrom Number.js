/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const string = String(x);
    const arr = Array.from(string);
    const rev = arr.reverse();
    const newStri = rev.join("");
    return Number(newStri) === x ? true: false;
};