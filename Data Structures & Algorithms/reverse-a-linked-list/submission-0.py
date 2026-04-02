# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        if(not head):
            return None
        cursor = head
        stack.append(cursor)
        while(cursor and cursor.next):
            print("cursor", cursor.val)
            cursor = cursor.next
            stack.append(cursor)

        print("STACK: ", stack)

        output = None
        output_cursor = None
        while(stack):
            evaluate = stack.pop()
            if(not output):
                output = ListNode(evaluate.val)
                output_cursor = output
            else:
                print("cursor_output", output_cursor.val)
                output_cursor.next = ListNode(evaluate.val)
                output_cursor = output_cursor.next
        return output
