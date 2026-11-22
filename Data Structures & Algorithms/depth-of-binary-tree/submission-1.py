# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left = right = 1
        if root is None:
            return 0
        if root.left:
            left = self.maxDepthCount(root.left) + 1
        if root.right:
            right = self.maxDepthCount(root.right) + 1
        return max(left, right)

    def maxDepthCount(self, root: Optional[TreeNode], cnt:int = 1) -> int:
        left = right = 1
        if root.left:
            left += self.maxDepthCount(root.left, left + 1)
        if root.right:
            right += self.maxDepthCount(root.right, right + 1)
        print("returning",root.val ,max(left, right))
        return max(left, right)
