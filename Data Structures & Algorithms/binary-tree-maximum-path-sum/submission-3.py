# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val

        def dfs(node):
            if not node:
                return 0
            
            pathVal = node.val + dfs(node.left) + dfs(node.right)
            nonlocal maxPath
            maxPath = max(maxPath, pathVal)

            childVal = max(dfs(node.left), dfs(node.right))
            if childVal < 0:
                childVal = 0
            maxPath = max(maxPath, node.val + childVal)
            return node.val + childVal

        dfs(root)
        return maxPath