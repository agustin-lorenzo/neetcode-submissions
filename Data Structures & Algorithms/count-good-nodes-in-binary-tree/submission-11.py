# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        
        def dfs(node, prevMax):
            if not node:
                return
            nonlocal result
            
            if node.val >= prevMax:
                result += 1

            newMax = max(prevMax, node.val)
            dfs(node.left, newMax)
            dfs(node.right, newMax)
        
        dfs(root, float("-inf"))
        return result