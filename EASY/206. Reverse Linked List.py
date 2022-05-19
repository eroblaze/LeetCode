# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        
        while head != None:
            l.append(ListNode(head.val))
            head = head.next
        if l:   
            l.reverse()
            first = l[0]
            l.pop(0)
            current = first

            for i in l:
                current.next = i
                current = current.next

            print(first, current)
            return first
        else: return ListNode().next