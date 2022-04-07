/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const res = [];
    
    for(let i = 0; i < s.length; i++) {
        if (s[i] === ")" && res[res.length-1] === "(" || s[i] === "]" && res[res.length-1] === "[" || s[i] === "}" && res[res.length-1] === "{") {
            res.pop();
        } else {
            res.push(s[i]);
        }
    }
    
    const isEmpty = !Boolean(res.length);
    return isEmpty;
};