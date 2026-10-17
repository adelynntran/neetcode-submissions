# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower, node, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return (
                dfs(lower, node.left, node.val) #val > left
                and
                dfs(node.val, node.right, upper) #val < right
            )
        return dfs(float("-inf"), root, float("inf"))
        
        