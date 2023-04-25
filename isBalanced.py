# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# depth helper method
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node: 
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if abs(left-right)>1: 
                res = False
            return 1+max(left, right)
        
        res = True
        depth(root)
        return res
