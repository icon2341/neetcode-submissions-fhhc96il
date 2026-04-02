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
        self.printHead(head)
        while True:
            # we have found our kth value
            kth = self.getKth(groupPrev,k)
            # lets start reversing

            if(not kth):
                break

            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

            self.printHead(dummy)

        return dummy.next

    
    def printHead(self, head):
        curr_head = head
        listRep = []
        while(curr_head):
            listRep.append(curr_head.val)
            curr_head = curr_head.next

        print(listRep)


    def getKth(self, curr, k):
        """
        Helper function to jump exactly 'k' nodes ahead.
        Returns the kth node, or None if there are fewer than k nodes left.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr