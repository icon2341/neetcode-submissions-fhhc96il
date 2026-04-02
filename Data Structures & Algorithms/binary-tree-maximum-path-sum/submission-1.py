# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize to negative infinity to handle trees with all negative numbers
        self.global_max = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Step 1: Recursively get the max "Straight Line" from left and right children.
            # The max(..., 0) fixes the Negative Number Trap. If a branch is negative, we ignore it.

            # Left_gain is the left value then the path down to the base
            # that only prioritizes higher non negative value.
            left_gain = max(dfs(node.left), 0)

            # i.e we go through the left child and zig zag BUT NEVER BRANCh
            # down to the root making good choices.
            right_gain = max(dfs(node.right), 0)

            # Step 2: The "Inverted U" (Your old DFS logic)
            # Here is where we consifer the branching and we use this to combine
            # two best paths of the left and right child
            current_peak = node.val + left_gain + right_gain
            
            # We basically only use that number when we are checking to see if we won
            # otherwise we return the parent plus the BEST child not both
            self.global_max = max(self.global_max, current_peak)

            # All we are doing here is returning the parent PLUS the best choice
            # for the parent. NO BRANCHING, we just want to return the best path up.
            return node.val + max(left_gain, right_gain)

        # Kick off the traversal from the root
        dfs(root)

        return self.global_max

"""
Redo this

So the way this works is kind of interesting

Within the recursive DFS node, we basically understand that a path has two sates.

Branching and straight line. A Upside Down U (branching) and then the continuous path.

And we want to return the Straight line to the parent that it could take.

But only use the root parent value itself pus the SOM of the straight lines of the childeren

When ever we are determining if we need to UPDATE the max or not.

Imnot sure how consise of a description that was.

"""