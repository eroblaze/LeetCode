# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # It has to be linear time
        if not head.next:
            return head.next
        
        list_arr = []
        current = head
        while current:
            list_arr.append(ListNode(current.val))
            current = current.next
        # list_arr contains all the nodes
        list_arr.pop(-n)
        new_head = list_arr[0]
        current = new_head
        for i in range(1, len(list_arr)):
            current.next = list_arr[i]
            current = current.next
        
        return new_head
        