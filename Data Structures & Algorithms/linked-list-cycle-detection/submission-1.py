# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointer approach fast or slow
        # the Fast pointer will complete the cycle TWO times for every
        # ONE time that it takes the slow to go.


        if(not head):
            return False

        fastCursor = head
        slowCursor = head.next
        
        while(fastCursor and slowCursor):
            print("CURSOR", fastCursor.val, slowCursor.val)
            fastCursor = fastCursor.next
            if(slowCursor.next):
                slowCursor = slowCursor.next.next
            else:
                return False

            if(fastCursor == slowCursor):
                return True

        return False

                

            
