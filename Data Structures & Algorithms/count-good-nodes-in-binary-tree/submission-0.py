# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 1
        
        def dfs(root, prevMax):
            if not root:
                return
            nonlocal result
            leftMax, rightMax = prevMax, prevMax
            if root.left and root.left.val >= prevMax:
                leftMax = root.left.val
                result += 1
            if root.right and root.right.val >= prevMax:
                rightMax = root.right.val
                result += 1
            dfs(root.left, leftMax)
            dfs(root.right, rightMax)

        dfs(root, root.val)
        return result

        