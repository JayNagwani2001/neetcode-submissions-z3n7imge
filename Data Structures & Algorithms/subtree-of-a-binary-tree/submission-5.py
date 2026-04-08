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
        elif not p:
            return False
        elif not q:
            return False
            
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False

        # ans1 = False
        # if root.val == subRoot.val:

        ans1 = self.isSameTree(root, subRoot)

        # if ans1:
        #     return True
        if root.left:
            ans2 = self.isSubtree(root.left, subRoot)
            ans1 = ans1 | ans2 
        if root.right:
            ans2 = self.isSubtree(root.right, subRoot)
            ans1 = ans1 | ans2 

        return ans1

