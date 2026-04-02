# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Initialization
        # We use a dummy node to easily handle edge cases (like reversing the very first group)
        # dummy.next will eventually be the new head of our modified list.
        dummy = ListNode(0, head)
        
        # groupPrev points to the node IMMEDIATELY BEFORE the current k-group we are working on.
        # Initially, it's the dummy node.
        groupPrev = dummy

        while True:
            # 2. Identify the current k-group
            kth = self.getKth(groupPrev, k)
            
            # If we don't have a full group of k nodes left, we are done. Break out.
            if not kth:
                break 
            
            # groupNext points to the node IMMEDIATELY AFTER our current k-group.
            # We need to save this so we don't lose the rest of the list when we reverse the links.
            groupNext = kth.next 

            # 3. Reverse the current k-group
            # To reverse in place without breaking the chain, we initialize 'prev' to groupNext.
            # This ensures the first node of our group (which becomes the last) points to the rest of the list.
            prev = groupNext
            curr = groupPrev.next # curr is the first node in the current k-group
            
            # Standard linked list reversal loop, but we stop when curr reaches groupNext
            while curr != groupNext:
                tmp = curr.next    # Save the next node
                curr.next = prev   # Reverse the pointer
                prev = curr        # Move prev forward
                curr = tmp         # Move curr forward

            # 4. Reconnect the reversed group to the previous part of the list
            # At this point, the group is reversed, but groupPrev is still pointing to the OLD first node.
            
            # Save the old first node (which is now the last node of the reversed group).
            # We need this because it will become the 'groupPrev' for the NEXT iteration.
            tmp = groupPrev.next 
            
            # Connect the end of the previous group to the NEW first node of the reversed group (which is 'kth')
            groupPrev.next = kth 
            
            # Move groupPrev forward to prepare for the next k-group.
            groupPrev = tmp
            
        return dummy.next

    def getKth(self, curr, k):
        """
        Helper function to jump exactly 'k' nodes ahead.
        Returns the kth node, or None if there are fewer than k nodes left.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr