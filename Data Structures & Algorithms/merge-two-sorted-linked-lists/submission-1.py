# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        outputList = None
        outputListCursor = None

        if(not list1 and not list2):
            print("Returning Neither")
            return None
        elif(not list1):
            print("Returning list 2")
            return list2
        elif(not list2):
            print("Returning list 1")
            return list1

        list1Cursor = list1
        list2Cursor = list2
        while(list1Cursor and list2Cursor):
            if(not outputList):
                print("Pre", list1Cursor.val, list1Cursor.next, list2Cursor.val,list2Cursor.next)
                if(list1Cursor.val < list2Cursor.val):
                    outputList = ListNode(val=list1Cursor.val)
                    outputListCursor = outputList
                    list1Cursor = list1Cursor.next
                else:
                    outputList = ListNode(val=list2Cursor.val)
                    outputListCursor = outputList
                    list2Cursor = list2Cursor.next
            else:
                print("Post", list1Cursor.val, list2Cursor.val)
                if(list1Cursor.val < list2Cursor.val):
                    newNode = ListNode(list1Cursor.val)
                    outputListCursor.next = newNode
                    outputListCursor = outputListCursor.next
                    list1Cursor = list1Cursor.next
                else:
                    newNode = ListNode(list2Cursor.val)
                    outputListCursor.next = newNode
                    outputListCursor = outputListCursor.next
                    list2Cursor = list2Cursor.next

        while(list1Cursor):
            newNode = ListNode(list1Cursor.val)
            outputListCursor.next = newNode
            outputListCursor = outputListCursor.next
            list1Cursor = list1Cursor.next
        
        while(list2Cursor):
            newNode = ListNode(list2Cursor.val)
            outputListCursor.next = newNode
            outputListCursor = outputListCursor.next
            list2Cursor = list2Cursor.next

        return outputList
