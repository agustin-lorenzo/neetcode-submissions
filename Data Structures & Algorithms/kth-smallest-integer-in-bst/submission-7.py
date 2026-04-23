# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = -1
        counter = 0

        def dfs(node):
            nonlocal result
            nonlocal counter
            if not node or counter >= k:
                return
            
            dfs(node.left)
            if counter < k:
                result = node.val
                counter += 1
            dfs(node.right)
        
        dfs(root)
        return result