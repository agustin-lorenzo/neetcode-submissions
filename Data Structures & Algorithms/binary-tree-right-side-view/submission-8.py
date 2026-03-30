# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        def dfs(node, level):
            if not node:
                return
            
            if len(levels) < level + 1:
                levels.append([node.val])
            else:
                levels[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        result = []
        for l in levels:
            result.append(l[-1])
        
        return result
