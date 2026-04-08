# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder_dfs(self, root):
        if not root:
            return 
        self.inorder_dfs(root.left)
        self.arr.append(root.val)
        self.inorder_dfs(root.right)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.inorder_dfs(root)

        print(self.arr)

        return self.arr[k-1]
