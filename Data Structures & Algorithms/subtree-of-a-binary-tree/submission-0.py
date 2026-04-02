# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # determine if the sub root is truly a subroot of root

        # if the subRoot (which can be smaller) is empty return true
        if(not subRoot):
            return True

        # if the tree we are comparing to, then return false obviously
        if not root:
            return False

        # check to see if the two trees are the same
        if self.checkSame(root,subRoot):
            return True

        # if not then check to see if EITHER child of root is the same
        # and so on....
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))


    def checkSame(self, p,q):

        if(not p and not q):
            return True
        if(p and q and p.val == q.val):
            return self.checkSame(p.left,q.left) and self.checkSame(p.right,q.right)
        else:
            return False

