# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True

        # alternative is to return a tuple with baleneced and use that but thats too much work

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            if(abs(left-right)>1):
                self.res = False

            return max(left,right) +1

        dfs(root)

        return self.res

            