# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.right), self.height(root.left))

    def inorder(self, root, arr):
        if not root:
            return

        self.inorder(root.left, arr)

        left = self.height(root.left)
        right = self.height(root.right)

        arr.append(abs(left - right) <= 1)

        self.inorder(root.right, arr)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        arr = []

        self.inorder(root, arr)

        return all(arr)