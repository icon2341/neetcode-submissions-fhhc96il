"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # trick is to loop through and create a hash of every node
        # then link after, random would be null for now

        # use original node ID as key and new node ID as value

        nodes = {None: None}

        head_cursor = head

        while head_cursor:
            nodes[head_cursor] = Node(head_cursor.val, head_cursor.next, head_cursor.random)
            head_cursor = head_cursor.next

        # loop through each key in nodes and update pointers since we have all now

        for old_head in nodes.keys():
            if(not old_head):
                continue
            nodes[old_head].next = nodes[old_head.next]
            nodes[old_head].random = nodes[old_head.random]

        return nodes[head]

        
        
