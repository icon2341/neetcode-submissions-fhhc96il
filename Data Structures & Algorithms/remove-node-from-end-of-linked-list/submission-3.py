# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy node to handle edge cases (like removing the head)
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # 1. Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # 2. Move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # 3. Skip the desired node
        slow.next = slow.next.next

        return dummy.next


# Solution description:
"""
we need to get the nth node, we can trivially do this using fast and slow
all we have to do is offset fast by n first
then increment both by normal until slow is at the nth element frmo the end 
since fast was offset that much at hte beginning.

we then skip slow.next and do a splice for slow so it skips the nth value

and the only trick here is to add a fake node at the beginning (which we skip at the end) 
so that slow.next.next doesnt break
"""
