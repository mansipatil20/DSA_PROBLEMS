# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverseSubTree(currentRoot, subCurrentRoot):
            if not currentRoot and not subCurrentRoot:
                return True
            if not currentRoot or not subCurrentRoot:
                return False
            return (currentRoot.val == subCurrentRoot.val and 
            traverseSubTree(currentRoot.left, subCurrentRoot.left) and 
            traverseSubTree(currentRoot.right, subCurrentRoot.right))
        
        if not root:
            return False
        if traverseSubTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        