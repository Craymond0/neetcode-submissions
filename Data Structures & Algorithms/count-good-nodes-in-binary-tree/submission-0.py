# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxVal):
            res = 0
            if not root:
                return 0

            if root.val >= maxVal:
                res = 1
                maxVal = max(maxVal, root.val)
            
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)

            return res

            


        return dfs(root, root.val)