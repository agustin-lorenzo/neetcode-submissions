# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = 0

        def dfs(node):
            nonlocal count, result
            if not node:
                return
            
            dfs(node.left)
            if count < k:
                count += 1
                result = node.val
                dfs(node.right)
        
        dfs(root)
        return result