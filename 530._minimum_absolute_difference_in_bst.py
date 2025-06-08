# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.minDiff = float('inf')

        def findMin(node):
            if not node:
                return
            findMin(node.left)

            if self.prev != None:
                self.minDiff = min(self.minDiff, abs(node.val - self.prev))
            self.prev = node.val

            findMin(node.right)
        
        findMin(root)

        return self.minDiff
        