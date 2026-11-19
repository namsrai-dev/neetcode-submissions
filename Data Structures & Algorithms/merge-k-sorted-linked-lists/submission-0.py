# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            # print(lists)
            l1 = lists.pop()
            l2 = lists.pop()
            l3 = self.mergeLists(l1, l2)
            lists.append(l3)

        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = n = ListNode(0)
        while l1 or l2:
            if l1 and l2 and l1.val <= l2.val:
                n.next = l1
                l1 = l1.next
            elif l1 and l2 and l1.val > l2.val:
                n.next = l2
                l2 = l2.next
            elif l1:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next

            n = n.next
        return dummy.next
