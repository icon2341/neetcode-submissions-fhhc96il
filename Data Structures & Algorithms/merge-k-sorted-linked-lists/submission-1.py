# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # trivial approach is to turn all lists into 
        # one array, sort the array
        # turn back into list

        res = ListNode(0)
        cur = res

        while True:
            minNode = -1

            # loop through each of the list nodes
            for i in range(len(lists)):
                if not lists[i]:
                    # if a list node is empty
                    continue
                # if we have not initialized min node
                # set the minNode by comparing all three lists and finalizing the smallest
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
            # if minnode was not set meaning all were empty
            if minNode == -1:
                break
            # set the cursor next to the smallest list node of the lists that we set earlier
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next

        return res.next

"""
The solution is kind of interesting for zero space.

we create a new node and list

we loop through each listNode in the lists to find the smallest
if a listNode is empty then we skip it
we find the smallest by setting minNode for first non none list then comparing each
after to it

we then take that min node (index of the smallest list) and we append it to our dummy

we then return the dummy after we have exhausted all the lists. We know all lists are exhausted 
because all lists would be NONE meaning our minNode would be -1 which means it wasnt set and we can exit
"""
        
