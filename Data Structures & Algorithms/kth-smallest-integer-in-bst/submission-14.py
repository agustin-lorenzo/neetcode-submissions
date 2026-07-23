# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None

        def dfs(node):
            nonlocal result, k
            if not node or k == 0:
                return
            
            dfs(node.left)
            if k > 0:
                result = node.val
                k -= 1
            dfs(node.right)
        
        dfs(root)
        return result