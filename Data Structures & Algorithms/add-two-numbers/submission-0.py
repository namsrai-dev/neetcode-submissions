# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = m = 1
        num1 = num2 = 0
        while l1:
            num1 += n * l1.val
            n = n * 10
            l1 = l1.next
        while l2:
            num2 += m * l2.val
            m = m * 10
            l2 = l2.next
        dummy = n = ListNode(0)

        for i in reversed(str(num1 + num2)):
            n.next = ListNode(int(i))
            n = n.next
        return dummy.next
        
