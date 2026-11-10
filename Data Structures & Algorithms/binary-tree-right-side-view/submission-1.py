# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        arr = []

        if root:
            queue.append(root)

  
        while len(queue) > 0:

            size = len(queue)

            for i in range(len(queue)):

                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
                if i == size - 1:
                    arr.append(cur.val)        


        return arr