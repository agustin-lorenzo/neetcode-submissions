# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGood = 0

        def dfs(node, prevMax):
            nonlocal numGood
            if not node:
                return
            
            if node.val >= prevMax:
                numGood += 1
            currMax = max(prevMax, node.val)
            dfs(node.left, currMax)
            dfs(node.right, currMax)
        
        dfs(root, root.val)
        return numGood