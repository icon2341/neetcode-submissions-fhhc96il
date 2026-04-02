class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # if not atleast two values quit
        if not head or not head.next:
            return

        # 1. Find the middle using slow/fast pointers
        # We want slow to end up at the end of the FIRST half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and Reverse the second half
        second = slow.next
        slow.next = None # Properly sever the list
        
        prev = None
        curr = second
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # 3. Merge (Zip) the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2