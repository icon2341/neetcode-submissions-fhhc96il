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
