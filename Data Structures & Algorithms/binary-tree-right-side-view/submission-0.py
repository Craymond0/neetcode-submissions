# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])

        res = []

        while queue:
            qLen = len(queue)
            rightMost = None

            for i in range(qLen):
                node = queue.popleft()

                if node:
                    rightMost = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if rightMost:
                res.append(rightMost.val)

        return res

