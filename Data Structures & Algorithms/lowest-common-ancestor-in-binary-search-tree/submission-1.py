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

"""
I knew the solution and intuioton here
But i was confused as to how to traverse the tree
Either using recurison or Itteratively.

This would be solved by running through the problem tbh
Also it is BFS which is itterative.

But it doesnt use a stack, stack is just ONE way we can do BFS, since we are in a binary tree
We can traverse without stack instead of prioritising specific neighbors

"""

