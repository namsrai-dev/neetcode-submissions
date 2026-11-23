# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def getDepth(root) -> int:
            nonlocal res
            left = right = 0
            if root.left:
                left += getDepth(root.left)
            if root.right:
                right += getDepth(root.right)
            res = max(res, left+right)
            return 1 + max(left, right)

        getDepth(root)

        # res = max(res, left+right)

        return res

