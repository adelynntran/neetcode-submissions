# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            if not node:
                return False
            # add curr_sum to current node
            curr_sum += node.val

            # check if we add the bottom yet (check leaf):
            if not node.left and not node.right:
                return curr_sum == targetSum
            
            # either left OR right has the valid path:
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        
        return dfs(root, 0)

        