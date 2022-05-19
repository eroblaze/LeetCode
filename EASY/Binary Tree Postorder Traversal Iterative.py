# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        preorder_arr = []
        stack = [root]
        
        while stack:
            p_node = stack.pop()
            preorder_arr.append(p_node.val)
            
            if p_node.left: stack.append(p_node.left)
            if p_node.right: stack.append(p_node.right)
                
        return reversed(preorder_arr)