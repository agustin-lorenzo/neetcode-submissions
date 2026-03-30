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
            
            result = 0
            if node.val >= currentMax:
                result += 1
            currentMax = max(currentMax, node.val)
            result += dfs(node.left, currentMax)
            result += dfs(node.right, currentMax)
            return result

        return dfs(root, root.val)



            
