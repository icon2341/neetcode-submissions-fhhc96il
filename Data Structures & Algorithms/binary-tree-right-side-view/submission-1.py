# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        output = []

        while(queue):
            qLen = len(queue)
            # array but we only want to store the LAST element in this array
            level = None
            for i in range(qLen):
                node = queue.pop(0)
                if node:
                    level = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                output.append(level)
            print("LEVEL", level)

        return output

"""

Was able to do this all on my own, builds on previous solution with one trick,
instead of building a list, we just want the last seen value in each level
which is effectively the right most value. So instead of a level array, 
we just use a static int

"""