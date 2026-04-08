# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0
                    
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        
        return 1+max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        op1 = self.diameterOfBinaryTree(root.left)
        op2 = self.diameterOfBinaryTree(root.right)
        op3 = self.height(root.left) + self.height(root.right)

        ans = max(max(op1, op2), op3)

        return ans