"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # old to new
        # as we traverse we use the old node as key
        # new node as value
        # if we see the same neighbor again in any adj list
        old_to_new = {}

        def dfs(node):

            # base case is that this node is 
            # already in the dict
            # which means it was copied already
            # its neighbors might be incomplete but thats ok
            if node in old_to_new:
                return old_to_new[node]
            
            # create initial new node and store reference to it
            copy = Node(node.val)
            # insert new node into dict
            old_to_new[node] = copy

            # loop through each neighbor of old node and do the same to them
            for neighbor in node.neighbors:
                # update our refrence copys neighbors by running copier
                # neighbor and its neighbors 
                # eventually building out copies of all neighbors
                # and finally appending the copied neighbors into this node
                # which updates the dict since we are updating the reference of that node
                copy.neighbors.append(dfs(neighbor))
            # when you are done return the copied node which allows us to complete the recursion
            return copy

        return dfs(node) if node else None
                    




        