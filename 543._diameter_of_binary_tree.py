class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)

            # diameter is the sum of left and right subtree heights
            self.max_diameter = max(self.max_diameter, left + right)

            return max(left, right) + 1  # return height

        depth(root)
        return self.max_diameter
