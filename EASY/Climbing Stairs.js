/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
   if (n === 1) return 1;
    /*
      TrailingStep and currentStep track the total number of ways to get to that step.
      Initially, trailingStep represents step 1 and currentStep is step 2.
    */
    let trailingStep = 1;
    let currentStep = 2;
    let nextStep;
    for (let i = 2; i < n; i++) {
      nextStep = trailingStep + currentStep;
      [trailingStep, currentStep] = [currentStep, nextStep];
    }
    return currentStep;
};