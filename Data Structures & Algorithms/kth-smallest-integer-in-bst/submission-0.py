# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            if not node:
                return

            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res


"""
Traverse the tree in order.

Meaning Left (DATA) Right

The reason this works is because intutively its a BST

So left node is less than right node.

We just go through every node in order meaning we count left nodes before counting root
then we do right of root.

Kind of confusing but it intuitevely makes sense because.

"""




            


            

            
                

            

        

            