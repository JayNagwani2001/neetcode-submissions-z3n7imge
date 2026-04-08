# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, root):
        if not root:
            return
        if root.left and root.right:
            self.invert(root.left)
            self.invert(root.right)

            root.left, root.right = root.right, root.left
        elif root.left:
            self.invert(root.left)
            root.right = root.left
            root.left = None
        elif root.right:
            self.invert(root.right)
            root.left = root.right
            root.right = None
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.invert(root)

        return root