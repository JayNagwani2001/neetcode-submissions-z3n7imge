# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0 
    def dfs(self, root, max_val):
        # if not root.left and not root.right:
        if root.val >= max_val:
            self.count += 1
            # return 

        if root.left:
            self.dfs(root.left, max(root.val, max_val))
        if root.right:
            self.dfs(root.right, max(root.val, max_val))


    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, -1000000)

        return self.count