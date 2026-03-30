# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, currentMax):
            if not node:
                return 0
            
            if node.val >= currentMax:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)

            return dfs(node.left, currentMax) + dfs(node.right, currentMax)

        if root:
            return dfs(root, root.val)
        else:
            return 0



            
