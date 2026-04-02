# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # essentially we do it in reverse
        # root is always good
        # then as we traverse down, we tell each child its parents 
        # largest value seen.
        # if that value is larger then increment output
        # otherwise continue onwards

        self.output = 0

        def dfs(root, largestSeen):
            if(not root):
                return
            print("EVAL:",root.val, largestSeen )
            if(root.val >= largestSeen):
                self.output += 1
                dfs(root.left, root.val)
                dfs(root.right,root.val)
            else:
                dfs(root.left, largestSeen)
                dfs(root.right,largestSeen)

        dfs(root,float('-inf'))

        return self.output