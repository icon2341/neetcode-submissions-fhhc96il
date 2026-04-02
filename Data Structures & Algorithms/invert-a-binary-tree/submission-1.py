# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if null do nothing to avoid throwing error (base case)
        if(not root):
            return None
        
        # swap the kids
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # do this on the left childeren

        self.invertTree(root.left)

        # do this on the right childeren
        self.invertTree(root.right)

        return root
    