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
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


    """This solution was pretty easy with recursive DFS, 

    We simply do The recursion on BOTH at the same time with our base case
    being if BOTH are exhausted then we return True for that node
    
    however, if one os exhausted and one isnt, OR if at any point they have different values
    you must return False.

    And the recursion mechanism itself is,

    If both p and q exist and are the same, then evaluate if the same is true for the childeren of p and q
    and their childeren and so on.

    """

                
            
