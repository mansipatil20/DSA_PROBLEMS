class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Initialize the required pointers
        self.first = self.middle = self.last = self.prev = None

        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Check for BST violation
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    # First violation
                    self.first = self.prev
                    self.middle = node
                else:
                    # Second violation
                    self.last = node
            
            self.prev = node  # Update previous node
            inorder(node.right)

        inorder(root)

        # Fix the swapped nodes
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val
