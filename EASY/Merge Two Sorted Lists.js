/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    
    // First of all, get all the values in each linked list and put them in an array 
    let list1Array = [];
    let list2Array = [];
    
    
    const returnArray = (list) => {
        // Base case
        if (list.next == undefined) return [list.val];
        else {
            const res = returnArray(list.next);
            res.unshift(list.val);
            return res;
        }
        
    };
    
    list1Array = (list1 instanceof ListNode)? returnArray(list1): [];
    list2Array = (list2 instanceof ListNode)? returnArray(list2): [];
    
    const mergedArr = [...list1Array, ...list2Array].sort((a,b) => a-b);
    
    let returnNode;
    
    if (mergedArr.length) {
         returnNode = new ListNode(mergedArr[0]);

        let head = returnNode;

        for (let i = 1; i < mergedArr.length; i++) {
            const tempNode = new ListNode(mergedArr[i]);
            head.next = tempNode;
            head = head.next;
        }
    } else {
        const fake = new ListNode();
        returnNode = fake.next;
    }
   
    
    return returnNode;    
};