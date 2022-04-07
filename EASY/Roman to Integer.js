/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let num = 0;
    
    const obj = {
        I : 1,
        V : 5,
        X : 10,
        L : 50,
        C : 100,
        D : 500,
        M : 1000
    }
    
    for ( let i = 0; i < s.length; ) {
        if (s[i] === "I" || s[i] === "X" || s[i] === "C") {
            
            if (s[i] === "I" && s[i+1] === "V") {
                num += 4;
                i += 2;
            }
            else if (s[i] === "I" && s[i+1] === "X") {
                num += 9;
                i += 2;
            }
            else if (s[i] === "X" && s[i+1] === "L") {
                num += 40;
                i += 2;
            }
            else if (s[i] === "X" && s[i+1] === "C") {
                num += 90;
                i += 2;
            }
            else if (s[i] === "C" && s[i+1] === "D") {
                num += 400;
                i += 2;
            }
            else if (s[i] === "C" && s[i+1] === "M") {
                num += 900;
                i += 2;
            }
            else {
                num += obj[s[i]];
                i++;
            }
        }
        else {
            num += obj[s[i]];
            i++;
        }
    }
    
    return num;
    
};