# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNumbers = 0
        def isGoodNumber(node, maxNode):
            if not node:
                return
            if node.val >= maxNode:
                self.goodNumbers+=1
                maxNode = node.val
            isGoodNumber(node.left,maxNode)
            isGoodNumber(node.right,maxNode)
        isGoodNumber(root,root.val)
        return self.goodNumbers
        