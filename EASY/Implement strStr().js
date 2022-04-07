/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (needle.length === 0) return 0;
    if (haystack.length === 0) return -1;
    
    const regex = new RegExp(`${needle}`);
    
    const answer = regex.exec(haystack);
    
    if (!answer) return -1;
    else return answer.index;
};