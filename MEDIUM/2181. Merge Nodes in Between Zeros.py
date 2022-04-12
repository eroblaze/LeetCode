class Solution:
           
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_list, current = [], head
        
        while current is not None:
            if current.val == 0:
                val_list.append([])
            else:
                val_list[-1].append(current.val)
            current = current.next
            
        val_list.pop()    
        added = list(map(lambda el: sum(el), val_list))
        
        res = ListNode(added[0])
        added.pop(0)
        current = res
        
        for i in added:
            current.next = ListNode(i)
            current = current.next
        
        return res