/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    // This problem is very similar to a fibonacci sequence problem question
    
    // base case
    
    if (strs.length === 1) return strs[0];
    
    else {
        const res = longestCommonPrefix(strs.slice(1));
        const first = strs[0];
        let theMatch = "";
        
        for (let i = 0; i < res.length; i++) {
            if (res[i] === first[i]) {
                theMatch += res[i];
            } else {
                break;
            }
        }
        
        return theMatch;
    }
    
};