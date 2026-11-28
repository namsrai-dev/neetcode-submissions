# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        elif not root or not subRoot:
            return False

        isTrue = self.sameTree(root, subRoot)
        if isTrue:
            return True
         
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, p, q):
        if not p and not q:
            return True

        if p and not q:
            return False

        if q and not p:
            return False

        if p and q and q.val != p.val:
            return False

        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        if left and right:
            return True

        return False

        