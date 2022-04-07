/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    if(!head) {
        const res = new ListNode();
        return res.next;
    } 
    
    const rec = (theHead) => {
        if (theHead.next === null) {
            const ret = new Set();
            ret.add(theHead.val);
            return ret;
        } else {
            const res = rec(theHead.next);
            res.add(theHead.val);
            return res;
        }
    };
    
    const realArr = Array.from(rec(head)).reverse();
    let link = new ListNode(realArr[0]);
    let newHead = link;
    
    for (let i = 1; i < realArr.length; i++) {
        const newLink = new ListNode(realArr[i]);
        newHead.next = newLink;
        newHead = newHead.next;
    }
    
    return link;
};