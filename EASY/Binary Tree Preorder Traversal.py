# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        val = []
        rights = []
        current = root
        while current:
            val.append(current.val)
            if current.right:
                rights.append(current.right)
            current = current.left
            if not current and len(rights):
                current = rights.pop()
                
        print(val)
        return val
            