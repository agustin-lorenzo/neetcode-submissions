# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        store = []

        def dfs(node):
            if not node or len(store) == k:
                return

            dfs(node.left)
            if len(store) < k:
                store.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return store[-1]