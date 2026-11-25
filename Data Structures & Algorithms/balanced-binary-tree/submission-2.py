# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            # print("root value ->",root.val)            
            left_node = dfs(root.left)
            right_node = dfs(root.right)
            # print("here the check", root.val, [abs(left_node[1] - right_node[1]) <= 1, max(left_node[1], right_node[1]) + 1])
            if left_node[0] == False or right_node[0] == False:
                return[False, max(left_node[1], right_node[1]) + 1]

            return [abs(left_node[1] - right_node[1]) <= 1, max(left_node[1], right_node[1]) + 1]

        return dfs(root)[0]
