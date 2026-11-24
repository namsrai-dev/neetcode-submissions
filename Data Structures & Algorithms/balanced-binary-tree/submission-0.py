# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        left = 0
        right = 0

        if not root:
            return True

        if root.left:
            left = self.getDepth(root.left)

        if root.right:
            right = self.getDepth(root.right)

        if -1 > left - right or left - right > 1:
            return False

        return True

    def getDepth(self, root) -> int:
        left = right = 1
        if root.left:
            left += self.getDepth(root.left)
        if root.right:
            right += self.getDepth(root.right)
        
        return max(left, right)
