# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build(self, root, pre, ino):
        if not pre or not ino:
            return
        node = pre[0]
        mid = ino.index(node)
        if not root:
            root = TreeNode()
        root.val = node

        #left
        self.build(root.left, pre[1:mid+1], ino[:mid])
        self.build(root.right, pre[mid+1:], ino[mid+1:])
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root

