# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # this is a BST
        # we want to find some node
        # where:
        # p is less than our node
        # q is higher than our node (or vise versa)
        # or p == node or q == node (whichever is higher)
        # if both p and q is higher than node, then we traverse right
        # otherwise traverse left

        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: 
                cur = cur.left
            else:
                return cur

