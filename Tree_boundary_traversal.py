class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        borderList = []

        def isLeaf(node):
            return node.left is None and node.right is None

        def addLeftBoundary(node):
            while node:
                if not isLeaf(node):
                    borderList.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        def addLeaves(node):
            if isLeaf(node):
                borderList.append(node.data)
                return
            if node.left:
                addLeaves(node.left)
            if node.right:
                addLeaves(node.right)

        def addRightBoundary(node):
            tmp = []
            while node:
                if not isLeaf(node):
                    tmp.append(node.data)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            borderList.extend(reversed(tmp))

        if not isLeaf(root):
            borderList.append(root.data)

        addLeftBoundary(root.left)
        addLeaves(root)
        addRightBoundary(root.right)

        return borderList
