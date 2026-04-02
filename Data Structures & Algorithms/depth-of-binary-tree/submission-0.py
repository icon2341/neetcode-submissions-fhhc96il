# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0

        # originally i did sum of both but thats actually counting the number of nodes in the tree
        # if we want MAX depth, then we would just pick the larger branch of the two 
        #  and return that. This would have been avoided by running through the problem by hand
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1