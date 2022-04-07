/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    // the Number.toString() method takes in a radix(), when you input a "2", it converts the number from a decimal into a binary number
    
    // Third method - made use of loops
    
    let binArr = [];
    let smallest = a.length > b.length? b: a;
    let biggest = a.length > b.length? a: b;
    let extra = 0;
    
    for (let i = biggest.length-1, j = smallest.length-1; i >= 0; i--) {
        if (j >= 0) {
            
            if ((+biggest[i] + extra)+ +smallest[j] > 1) {
                console.log("in the first")
                const sum = (+biggest[i] + extra)+ +smallest[j];
                const toPush = sum % 2;
                const rem = parseInt((sum/2));                
                 binArr.push(toPush);
                 extra = rem;
            } else {
                binArr.push((+biggest[i] + extra)+ +smallest[j]);
                extra = 0;
            }
            
            j--;

        } else {
            if (+biggest[i] + extra > 1) {
                binArr.push(0);
                extra = 1;
            } else {
                binArr.push(+biggest[i]+ +(extra));
                extra = 0;
            }
        }
        
    }
    
    if (extra) binArr.push(extra);
    binArr.reverse();
    const res = binArr.join("");
    return res;    
        
};