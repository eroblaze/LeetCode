/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (+x <= 1) {
        return x;
    };
    let middle = parseInt((x / 2));
    let answer = 0;
    let i = 1;
    
     while (!answer) {

        if ((i * i <= x) && ((i+1) * (i+1) > x)) {
            answer = i;
         }
         i++;
    }
    
    return answer;
};