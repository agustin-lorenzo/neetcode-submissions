# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0, 0]
            
            left, right = dfs(node.left), dfs(node.right)
            diameter = max([left[1], right[1], left[0] + right[0]])
            return [1 + max(left[0], right[0]), diameter]
        
        return dfs(root)[1]