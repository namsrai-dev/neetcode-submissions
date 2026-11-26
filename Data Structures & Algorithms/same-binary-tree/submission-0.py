# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p and q:
            print("this returning false1")
            return False
        
        elif not q and p:
            print("this returning false2")
            return False

        elif q.val != p.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        print("left right", left, right, p.val)

        if left == False or right == False:
            return False

        return True
        
        