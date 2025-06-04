# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfsTree(root):
            if not root:
                return 0
            lt = dfsTree(root.left)
            if lt == -1:
                return -1
            rt = dfsTree(root.right)
            if rt == -1:
                return -1
            
            if (abs(lt - rt) > 1):
                return -1
            
            return max(lt, rt) +1

        
        return dfsTree(root) != -1


        