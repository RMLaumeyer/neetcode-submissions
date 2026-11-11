# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathsum(self, root, target):

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == target

        if root.left:
            if self.pathsum(root.left, target - root.val):
                return True 

        if root.right:
            if self.pathsum(root.right, target - root.val):
                return True 

        return False


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.pathsum(root, targetSum)        
