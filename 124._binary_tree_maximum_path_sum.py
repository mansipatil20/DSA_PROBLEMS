# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxCount = float('-inf')

        def maxPathDown(node):
            if not node:
                return 0
            left = max(0,maxPathDown(node.left))
            right = max(0, maxPathDown(node.right))
            self.maxCount = max(self.maxCount, left+ right +node.val)
            return max(left, right) + node.val

        maxPathDown(root)
        return self.maxCount

        