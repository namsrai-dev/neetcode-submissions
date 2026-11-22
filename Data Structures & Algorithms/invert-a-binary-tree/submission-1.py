# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        queue = deque([root])
        while queue:
            my_root = queue.popleft()
            left = my_root.left
            my_root.left = my_root.right
            my_root.right = left
            if my_root.left:
                queue.append(my_root.left)
            if my_root.right:
                queue.append(my_root.right)

        return root