# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, prevMax):
            if not node:
                return 0

            numGood = 0
            if node.val >= prevMax:
                prevMax = node.val
                numGood += 1
            return numGood + dfs(node.left, prevMax) + dfs(node.right, prevMax)
        
        return dfs(root, float("-inf"))
