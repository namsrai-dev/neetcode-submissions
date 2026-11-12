# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head1, head2 = self.split_half(head)
        temp = head2
        dummy = ListNode()
        n = dummy
        prev = None
        while head2:
            next = head2.next
            head2.next = prev
            prev = head2
            head2 = next            

        head = self.concat(head1, prev)


    def split_half(self, head):
        if head is None or head.next is None:
            return head, None

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None  # cut the list
        return head, second

    def concat(self, a, b):
        dummy = tail = ListNode(None)
        while a and b:
            tail.next, a = a, a.next
            tail = tail.next
            tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next





