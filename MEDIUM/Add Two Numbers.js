/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
//     const num1Arr = [];
//     const num2Arr = [];
    
//     let present = l1;
//     while (true) {
//         num1Arr.push(present.val);
//         if (present.next == undefined) {
//             break;
//         }
//         present = present.next;
//     }
    
//     present = l2;
    
//      while (true) {
//         num2Arr.push(present.val);
//         if (present.next == undefined) {
//             break;
//         }
//         present = present.next;
//     }
    
    
//     I've gotten the two numbers in the array
    
//     let newnum1 = num1Arr.reverse();
//      let newnum2 = num2Arr.reverse();
    
//     newnum1 = Number(newnum1.join(""));
//     newnum2 = Number(newnum2.join(""));

//     const added = newnum1 + newnum2;
//     let addedArr = Array.from(String(added));
//     addedArr = addedArr.reverse();
    
//     const nodeArr = []; // [node1, node2, node3];
    
//     for (let el of addedArr) {
//         const node = new ListNode(Number(el));
//         nodeArr.push(node);
//     }
//     const realHead = nodeArr[0];
//     let head = realHead;
        
//     for (let i = 1; i < nodeArr.length; i++) {
//         head.next = nodeArr[i];
//         head = nodeArr[i];
//     }
    
//     return realHead;
    
    
    let node = null
    const carry = arguments[2]
    if (l1 || l2) {
        const val1 = l1 ? l1.val : 0
        const val2 = l2 ? l2.val : 0
        const next1 = l1 ? l1.next : null
        const next2 = l2 ? l2.next : null
        const val = carry ? val1 + val2 + 1 : val1 + val2
        node = new ListNode(val % 10)
        node.next = addTwoNumbers(next1, next2, val >= 10)  
    } else if (carry) {
        node = new ListNode(1)
        node.next = null
    }
    return node
    
    
};