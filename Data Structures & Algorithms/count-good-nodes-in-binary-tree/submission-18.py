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
            
            numGood = 1 if node.val >= prevMax else 0
            newMax = max(node.val, prevMax)

            left, right = dfs(node.left, newMax), dfs(node.right, newMax)
            numGood += left + right
            return numGood
        
        return dfs(root, float("-inf"))