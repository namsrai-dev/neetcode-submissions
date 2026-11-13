# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        prev = None

        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

        counter = 1
        curr = prev
        old = None
        while counter < n:
            print("curr", curr)
            old = curr
            curr = curr.next
            counter += 1
        print("old",old)
        # print(cur)
        if old is not None:
            old.next = curr.next
        else:
            curr = None

        temp = prev
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

        return prev
