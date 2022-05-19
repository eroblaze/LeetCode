# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def quick_sort(self, array):
        if len(array) <= 1:
            return array
        
        predicate = array[0]
        left = []
        right = []
        
        for i in array[1:]:
            if i <= predicate: left.append(i)
            else: right.append(i)
                
        l = self.quick_sort(left)
        r = self.quick_sort(right)
                
        return l + [predicate] + r
        
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use quick sort to group everything in one array and convert to a linked list
        
        new_list = []
        
        current = None
        for i in range(len(lists)):
            if (lists[i]):
                current = lists[i]
                while current:
                    new_list.append(current.val)
                    current = current.next

        to_llist = self.quick_sort(new_list)
        
        if to_llist:
            head = ListNode(to_llist[0])
            current = head
            if len(to_llist) > 1:
                for i in to_llist[1:]:
                    current.next = ListNode(i)
                    current = current.next

            return head
        else:  return ListNode().next
            